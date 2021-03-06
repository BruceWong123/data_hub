
from app.views.data_service import parse_single_frame
import logging
import threading
from datetime import datetime
import mysql.connector as mysql
import six.moves.urllib as urllib
from pymongo import MongoClient
import configparser
import pprint
import copy
import zlib
import base64
import time
import ast
import os
import redis
import google.protobuf.text_format as text

from app.views.traj.handle_attribute import handle_attribute
from app.views.traj.map_api import HDMap
from app.views.deeproute_perception_obstacle_pb2 import PerceptionObstacles
from app.views.deeproute_prediction_obstable_pb2 import PredictionObstacles
logger = logging.getLogger('django')


class DBManager(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath(
            os.path.dirname(__file__)) + "/config.ini")
        self.connect_to_mongodb()
        self.connect_to_mysql()
        # self.connect_to_redis()
        self.lock = threading.RLock()

    def connect_to_redis(self):
        host = self.config.get("Redis", "host")
        port = self.config.get("Redis", "port")
        pool = redis.ConnectionPool(
            host=host, port=port, password="123451", decode_responses=True)
        self.redis_cli = redis.Redis(connection_pool=pool)
        self.redis_cli.set('test', 'Successfully connected to Redis!')
        print(self.redis_cli.get('test'))

    def connect_to_mongodb(self):
        host = self.config.get("MongoDB", "host")
        if host == "10.3.3.45":
            logger.info("use cloud mongodb")
        elif host == "10.9.9.9":
            logger.info("use infra mongodb")
        port = self.config.get("MongoDB", "port")
        database = self.config.get("MongoDB", "database")
        username = urllib.parse.quote_plus(self.config.get("MongoDB", "user"))
        password = urllib.parse.quote_plus(
            self.config.get("MongoDB", "password"))
        authSource = "datahub"
        self.my_mongo_client = MongoClient(
            "mongodb://%s:%s@%s:%s/%s" % ('deep',
                                          'route', host, port, authSource)
        )
        self.mongo_db = self.my_mongo_client[database]
        print(
            "Successfully connected to Mongo : %s"
            % self.my_mongo_client.list_database_names()
        )

    def connect_to_mysql(self):
        host = self.config.get("MySQL", "host")
        port = self.config.get("MySQL", "port")
        database = self.config.get("MySQL", "database")
        username = urllib.parse.quote_plus(self.config.get("MySQL", "user"))
        password = urllib.parse.quote_plus(
            self.config.get("MySQL", "password"))
        self.mysql_db = mysql.connect(
            host=host, port=port, database=database, user=username, password=password
        )
        self.mysql_cursor = self.mysql_db.cursor()
        print(
            "Successfully Connected to remote MySQL : %s"
            % self.mysql_db.get_server_info()
        )

    def close_mysql(self):
        self.mysql_cursor.close()
        self.mysql_db.close()

    def get_mongo(self):
        return self.mongo_db

    def get_mysql(self):
        return self.mysql_db

    def _translate_topic(self, topic):
        if topic == 'perception':
            return '/perception/objects'
        elif topic == 'vs':
            return '/canbus/car_state'
        elif topic == 'signals_response':
            return '/perception/signals_response'
        elif topic == 'context':
            return '/planner/context'
        elif topic == 'debug_info':
            return '/planner/debug_info'
        elif topic == 'routing_request':
            return '/planner/routing_response'
        else:
            return topic

    def _assemble_topic_with_version(self, topic, version):
        if version != "" and version != "default_version":
            topic = topic + '_' + version
        return topic

    def _assemble_message_with_version(self, message, version):
        if version != "" and version != "default_version":
            message = message + '_' + version
        return message

    def get_all_timestamps_by_id(self, bagid):
        bag_association = bagid + "_association"
        # redis_result = self.redis_cli.get(bag_association)
        # if redis_result is not None:
        #     logger.info("found in redis")
        #     return redis_result
        logger.info("try to get lock for association")
        self.lock.acquire()
        logger.info("got into association lock")
        result = ""
        self.connect_to_mysql()
        sql = "SELECT association FROM app_association WHERE bagid = %s"
        adr = (bagid, )
        self.mysql_cursor.execute(sql, adr)
        query_result = self.mysql_cursor.fetchall()
        for row in query_result:
            result += " "
            result += str(row[0])
        logger.info("done mysql ")
        self.close_mysql()
        self.lock.release()
        # if len(query_result) > 0:
        #     self.redis_cli.set(bag_association, result)
        logger.info("release lock")

        return result

    def get_all_bag_id(self):
        # all_bag_id = "all_bag_id"
        # redis_result = self.redis_cli.get(all_bag_id)
        # if redis_result is not None:
        #     logger.info("found in redis")
        #     return redis_result
        logger.info(" try to get all bag id lock")
        self.lock.acquire()
        logger.info("into lock at:")
        localtime = time.asctime(time.localtime(time.time()))
        logger.info(localtime)
        result = ""
        db_messages = self.mongo_db["messages"]
        try:
            self.connect_to_mysql()
            sql = "SELECT bagid FROM app_bag"
            self.mysql_cursor.execute(sql)
            query_result = self.mysql_cursor.fetchall()
            logger.info("mysql bags number: ")
            logger.info(len(query_result))
            for row in query_result:
                result += " "
                result += str(row[0])
        except Exception as e:
            logger.info(e)
        finally:
            self.close_mysql()
            self.lock.release()
        logger.info("leave lock at:")
        localtime = time.asctime(time.localtime(time.time()))
        logger.info(localtime)
        # self.redis_cli.set(all_bag_id, result)
        return result

    def check_if_bag_exists(self, bagid):

        print("check bag {}".format(bagid))
        self.lock.acquire()
        self.connect_to_mysql()
        sql = "SELECT bagid FROM app_bag WHERE bagid = %s"
        adr = (bagid, )
        self.mysql_cursor.execute(sql, adr)
        mysql_query_result = self.mysql_cursor.fetchall()
        self.close_mysql()
        self.lock.release()
        # db_messages = self.mongo_db["messages"]
        # mongo_query_result = db_messages.find({"bagid": bagid, })

        for row in mysql_query_result:
            print(str(row[0]))

        result_len = len(mysql_query_result)
        print(" result len : {}".format(result_len))

        if len(mysql_query_result) == 0:
            return False
        else:
            return True

    def remove_all_data_by_id(self, bagid):
        if self.check_if_bag_exists(bagid):
            logger.info("into delete")
            self.lock.acquire()
            self.connect_to_mysql()
            sql = "DELETE FROM app_bag WHERE bagid = %s"
            adr = (bagid, )
            sql2 = "DELETE FROM app_association WHERE bagid = %s"
            adr2 = (bagid, )
            try:
                self.mysql_cursor.execute('SET FOREIGN_KEY_CHECKS=0;')
                self.mysql_cursor.execute(sql, adr)
                self.mysql_cursor.execute(sql2, adr2)
                self.mysql_db.commit()
                self.mysql_cursor.execute('SET FOREIGN_KEY_CHECKS=1;')
            except Exception as e:
                self.mysql_db.rollback()
                logger.info("exception")
                return False
            finally:
                self.close_mysql()
                self.lock.release()
            db_messages = self.mongo_db["messages"]
            db_messages.delete_many({"bagid": bagid})
            logger.info("done")
            return True
        else:
            return False

    def get_frame_by_id_time(self, bagid, timestamp):
        result = "no data found"
        db_messages = self.mongo_db["messages"]
        query_result = db_messages.find({"bagid": bagid, "topic": {
            "$regex": "^/perception/objects"}}).limit(10)
        for x in query_result:
            result = x["message"] + "||||||"
        return result

    def get_message_by_id_time_topic_version(self, bagid, timestamp, topic, version):
        logger.info("get message by id time topic..........")
        result = ""
        db_messages = self.mongo_db["messages"]
        topic_field_name = self._assemble_topic_with_version("topic", version)
        message_field_name = self._assemble_message_with_version(
            "message", version)
        topic_to_find = self._translate_topic(topic)
        logger.info("send out query to mongo ..........")
        query_result = db_messages.find(
            {"bagid": bagid, "timestamp": timestamp, topic_field_name: topic_to_find})

        for x in query_result:
            result = x[message_field_name]

        logger.info("get back from mongo and return..........")
        return result

    def get_range_message_by_id_topic(self, bagid, topic, start, end):
        logger.info("get message by id: {} topic : {} start : {} end: {}....".format(
            bagid, topic, start, end))
        result = ""
        topic = self._translate_topic(topic)
        db_messages = self.mongo_db["messages"]
        start_time = time.time()
        query_result = db_messages.find(
            {"bagid": bagid, "timestamp": {'$lte': end, '$gte': start}, "topic": topic}).sort("timestamp")
        index = 0
        for i, x in enumerate(query_result):
            result += x['timestamp'] + "timestamp_and_message" + x['message']
            if i != query_result.count() - 1:
                result += "deep_route"
            logger.info(
                "get frame for id : {} at index : {}".format(bagid, index))
            index += 1
        end_time = time.time()
        logger.info("get {} data consumed {:.2} s".format(topic,
                                                          end_time - start_time))
        return result

    def upload_message_by_id_time_topic_version(self, topic_message_pair, bagid, timestamp, topic, version):
        db_bag_data = self.mongo_db["messages"]
        topic_field_name = self._assemble_topic_with_version(topic, version)
        message_field_name = self._assemble_message_with_version(
            "message", version)

        data_dict = {}
        data_dict[topic_field_name] = list(topic_message_pair.keys())[0]
        data_dict[message_field_name] = list(topic_message_pair.values())[0]

        query_result = db_bag_data.find_one(
            {"bagid": bagid, "timestamp": timestamp})
        if query_result is None:
            metadata_dict = {
                "bagid": bagid,
                "timestamp": timestamp,
            }
            db_bag_data.insert_one({**metadata_dict, **data_dict})
        else:
            db_bag_data.update(
                {
                    "_id": query_result.get('_id')
                }, {
                    "$set": data_dict
                }
            )

# trajectory related
    def get_trajectoryinfo_by_id(self, bagid):

        db_task_data = self.mongo_db["tasks"]
        query_result = db_task_data.find_one({"taskid": taskid})
        if query_result is None:
            return {}
        else:
            data_dict = {
                "taskid": taskid,
                "play_mode": query_result.get("play_mode"),
                "scene_id": query_result.get("scene_id"),
                "subscene_id": query_result.get("subscene_id"),
                "planning_version": query_result.get("planning_version"),
                "perception_version": query_result.get("perception_version")
            }
            return data_dict

    def read_info_by_proto(self, filename, proto_format):
        if filename.split(".")[-1] == "bin":
            with open(filename, "rb") as f:
                proto_info = proto_format.FromString(f.read())
        elif filename.split(".")[-1] == "cfg" or filename.split(".")[-1] == "txt":
            with open(filename, "r") as f:
                proto_info = text.Parse(f.read(), proto_format)
        else:
            raise ValueError("unknown format!")
        return proto_info

    def evaluate_trajectories(self, bagid):
        print("evaluating ")

        db_traj_data = self.mongo_db["trajectories"]

        query_result = db_traj_data.distinct("timestamp")

        print(len(query_result))
        if query_result is not None:
            for i, x in enumerate(query_result):
                print(x)
        obj_type = "xxx"
        obj_id = "xxx"
        document_context = dict()
        points = []
        lane_ids = []
        data_path = "/home/bruce/datahub/data_hub/app/views/"
        map_path = os.path.join(data_path, "baoan-map_1207.bin")
        print("map path %s" % map_path)
        hdmap = HDMap(map_path)
        print("into handle attribute")
        handle_attribute(obj_type, obj_id, document_context,
                         points, lane_ids, hdmap)
        return

    def upload_trajectoryinfo_by_id(self, data, bagid):
        print("uploading....")

        result = {}
        db_traj_data = self.mongo_db["trajectories"]

        # perception_data = parse_single_frame()
        for perception_objects in perception_data:
            timestamp = perception_objects.time_measurement
            for prediction_object in perception_objects.prediction_obstacle:
                perception_object = prediction_object.perception_obstacle
                lane = prediction_object.feature[0].lane
                is_still = prediction_object.feature[0].is_still
                if len(lane.current_lane_feature) > 0:
                    lane_id = lane.current_lane_feature[0].lane_id
                else:
                    lane_id = -1
                data_dict = {}
                x, y, z = perception_object.position.x, perception_object.position.y, perception_object.position.z
                l, w, h = perception_object.length, perception_object.width, perception_object.height
                theta = perception_object.theta
                v_x, v_y = perception_object.velocity.x, perception_object.velocity.y
                a_x, a_y = perception_object.acceleration.x, perception_object.acceleration.y
                need_fields = [timestamp, x, y, z, l, w, h, theta, v_x, v_y, a_x, a_y,
                               lane_id, perception_object.type, is_still]

                data_dict["bagid"] = bagid
                data_dict["perception_object_id"] = perception_object.id
                data_dict["timestamp"] = timestamp
                data_dict["x"] = x
                data_dict["y"] = y
                data_dict["z"] = z
                data_dict["l"] = l
                data_dict["w"] = w
                data_dict["h"] = h
                data_dict["theta"] = theta
                data_dict["v_x"] = v_x
                data_dict["v_y"] = v_y
                data_dict["a_x"] = a_x
                data_dict["a_y"] = a_y
                data_dict["lane_id"] = lane_id
                data_dict["preception_object_type"] = perception_object.type
                data_dict["is_still"] = is_still
                query_result = db_traj_data.find_one(
                    {"bagid": bagid, "timestamp": timestamp, "perception_object_id": perception_object.id})
                # print(query_result)
                if query_result is None:
                    db_traj_data.insert_one(data_dict)
                else:
                    db_traj_data.update(
                        {
                            "_id": query_result.get('_id')
                        }, {
                            "$set": data_dict
                        }
                    )

    def get_trajectory_data(self, bagid, timestamp, objectid, seqlen):
        db_traj_data = self.mongo_db["trajectories"]
        query_result = db_traj_data.find(
            {"bagid": bagid, "timestamp": timestamp, "perception_object_id": objectid}).limit(seqlen)
        result = []
        if query_result is not None:
            for x in query_result:
                result.append(x)
        return result

# task related

    def get_taskinfo_by_id(self, taskid):
        db_task_data = self.mongo_db["tasks"]
        query_result = db_task_data.find_one({"taskid": taskid})
        if query_result is None:
            return {}
        else:
            data_dict = {
                "taskid": taskid,
                "play_mode": query_result.get("play_mode"),
                "scene_id": query_result.get("scene_id"),
                "subscene_id": query_result.get("subscene_id"),
                "planning_version": query_result.get("planning_version"),
                "perception_version": query_result.get("perception_version")
            }
            return data_dict

    def upload_task_info(self, taskid, play_mode, scene_id, subscene_id, planning_version, perception_version):
        db_task_data = self.mongo_db["tasks"]
        query_result = db_task_data.find_one({"taskid": taskid})
        metadata_dict = {
            "taskid": taskid
        }
        data_dict = {
            "play_mode": play_mode,
            "scene_id": scene_id,
            "subscene_id": subscene_id,
            "planning_version": planning_version,
            "perception_version": perception_version
        }
        if query_result is None:
            db_task_data.insert_one({**metadata_dict, **data_dict})
        else:
            db_task_data.update(
                {
                    "_id": query_result.get('_id')
                }, {
                    "$set": data_dict
                }
            )


# result related

    def upload_task_result_by_id_version_mode(self, data_dict, taskid, grading_version, play_mode):
        db_task_results = self.mongo_db["task_results"]
        query_result = db_task_results.find_one(
            {"taskid": taskid,  "grading_version": grading_version, "play_mode": play_mode})

        if query_result is None:
            metadata_dict = {
                "taskid": taskid,
                "grading_version": grading_version,
                "play_mode": play_mode
            }
            db_task_results.insert_one({**metadata_dict, **data_dict})

        else:
            db_task_results.update(
                {
                    "_id": query_result.get('_id')
                }, {
                    "$set": data_dict
                }
            )

    def get_task_result_by_id_version_mode(self, taskid, grading_version, play_mode):
        result = ""
        db_task_results = self.mongo_db["task_results"]
        query_result = db_task_results.find_one(
            {"taskid": taskid,  "grading_version": grading_version, "play_mode": play_mode})
        if query_result is not None:
            result = query_result.get('result')
        return result

    def upload_task_frame_result_by_id_version_time(self, data_dict, taskid, grading_version, timestamp):
        db_frame_results = self.mongo_db["frame_results"]
        query_result = db_frame_results.find_one(
            {"taskid": taskid,  "grading_version": grading_version, "timestamp": timestamp})

        if query_result is None:
            metadata_dict = {
                "taskid": taskid,
                "grading_version": grading_version,
                "timestamp": timestamp
            }
            db_frame_results.insert_one({**metadata_dict, **data_dict})
        else:
            db_frame_results.update(
                {
                    "_id": query_result.get('_id')
                }, {
                    "$set": data_dict
                }
            )

    def get_task_frame_result_by_id_version_time(self, taskid, grading_version, timestamp):
        db_frame_results = self.mongo_db["frame_results"]
        result = ""
        query_result = db_frame_results.find_one(
            {"taskid": taskid,  "grading_version": grading_version, "timestamp": timestamp})
        if query_result is not None:
            result = query_result.get('debug_info')
        return result

    def get_scene_result_aggregation(self, filters, sets, aggregation_methods):
        scene_result_data = self.mongo_db["frame_results"]
        pipeline = [{"$match": filters},
                    {"$project": aggregation_methods}]
        if len(sets) > 0:
            pipeline.insert(1, {"$addFields": sets})

        cursor = scene_result_data.aggregate(pipeline)
        res = list(cursor)
        scene_aggregation = self.mongo_db["scenes_aggregation_results"]
        if len(res) > 0:
            scene_aggregation.delete_many({})
            for result in copy.deepcopy(res):
                scene_aggregation.insert_one(result)
        return res

    def get_grading_result_aggregation(self, filters, aggregation_methods, projects):
        scene_aggregation_result = self.mongo_db["scenes_aggregation_results"]
        pipeline = [{"$match": filters},
                    {"$group": aggregation_methods}]
        if len(projects) > 0:
            pipeline.append({"$project": projects})

        cursor = scene_aggregation_result.aggregate(pipeline)
        res = list(cursor)
        return res

    def upload_scene_result_one(self, data_dict):
        db_frame_results = self.mongo_db["frame_results"]
        scene_data_dict = ast.literal_eval(data_dict["scene_result_one"])
        over_write = ast.literal_eval(data_dict["over_write"])
        query_result = db_frame_results.find_one({"play_mode": scene_data_dict["play_mode"],  "grading_config": scene_data_dict["grading_config"], "planning_version": scene_data_dict[
            "planning_version"], "prediction_version": scene_data_dict["prediction_version"], "scene_id": scene_data_dict["scene_id"], "car_id": scene_data_dict["car_id"]})
        if query_result is not None and over_write:
            db_frame_results.delete_one(query_result)
        if query_result is None or over_write:
            db_frame_results.insert_one(scene_data_dict)
