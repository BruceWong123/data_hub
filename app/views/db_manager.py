
import json
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
import pprint
from app.views.traj.handle_attribute import handle_attribute
from app.views.traj.map_api import HDMap
from app.views.deeproute_perception_obstacle_pb2 import PerceptionObstacles
from app.views.deeproute_prediction_obstable_pb2 import PredictionObstacles
from urllib.parse import quote_plus
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
        print("into connect to mongo")
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
        print("usename %s " % username)
        print("password %s " % password)
        print("host %s " % host)
        self.my_mongo_client = MongoClient(
            "mongodb://%s:%s@%s:%s/%s" % (username,
                                          password, host, port, authSource)
        )

        # # self.mongo_db = self.my_mongo_client[database]

        # # self.my_mongo_client = MongoClient(
        # #     'mongodb://root:iRJL3pbj05o0X3Y=@10.3.3.45:27017/datahub?authSource=admin')

        # self.my_mongo_client = MongoClient(
        #     'mongodb://root:iRJL3pbj05o0X3Y=@10.10.12.40:27017/datahub?authSource=admin')

        self.mongo_db = self.my_mongo_client['datahub']

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

    def get_all_bagids_trajectory(self):
        db_traj_data = self.mongo_db["trajectories"]
        bag_ids = db_traj_data.distinct("bagid")
        result = []
        for bag_id in bag_ids:
            print(bag_id)
            result.append(bag_id)
        return str(result)

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

    def insert_trajectory_attribute(self, document_contexts):
        print("inserting feature....")

        traj_features = self.mongo_db["features"]

        for key in document_contexts.keys():
            document_context = document_contexts[key]
            traj_features.update(
                {
                    "timestamp": key,
                    "bag_name": document_context["bag_name"]
                }, document_context, True
            )
        print("done insert")
        return

    def evaluate_trajectories(self, bagid, seqlen):
        logger.info("into evaluating ")

        db_traj_data = self.mongo_db["trajectories"]

        # timestamps = db_traj_data.distinct("timestamp")
        # object_ids = db_traj_data.distinct("perception_object_id")
        object_ids = db_traj_data.find(
            {"bagid": bagid}).distinct("perception_object_id")

        document_contexts = dict()

        # logger.info("len of ids: ", len(object_ids))

        count = 0
        curPath = os.path.abspath(os.path.dirname(__file__))
        map_path = os.path.join(curPath, "baoan-map_1207.bin")
        hdmap = HDMap(map_path)
        for object_id in object_ids:
            logger.info("evaluating: %s " % object_id)
            count = count+1
            object_data = db_traj_data.find(
                {"perception_object_id": object_id})

            object_data = [doc for doc in object_data]
            if len(object_data) < seqlen:
                print("no trajectory", object_id)
                continue
            print("has trajectory", object_id)
            points = []
            lane_ids = []

            for i in range(seqlen-1):
                x = object_data[i]
                points.append([x["x"], x["y"]])
                lane_ids.append(x["lane_id"])

            for i in range(len(object_data) - seqlen):
                data = object_data[i]
                timestamp = data["timestamp"]

                obj_type = data["preception_object_type"]
                obj_id = data["perception_object_id"]
                points.append([data["x"], data["y"]])
                lane_ids.append(data["lane_id"])

                document_context = dict()
                if timestamp in document_contexts:
                    document_context = document_contexts[timestamp]
                else:
                    document_context['bag_name'] = bagid
                    document_context['timestamp'] = timestamp
                    document_context['ids'] = []
                    document_context["turn"] = []
                    document_context['is_still'] = []
                    document_context["on_lane"] = []
                    document_context["lane_change"] = []
                    document_context["on_crosswalk"] = []
                    document_context["in_junction"] = []
                    document_contexts[timestamp] = document_context
                handle_result = handle_attribute(obj_type, obj_id, document_context,
                                                 points, lane_ids, hdmap)
                del points[0]
                del lane_ids[0]

        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(document_contexts)
        if len(document_contexts) > 0:
            print("dict size ", len(document_contexts))
            self.insert_trajectory_attribute(document_contexts)
        return "done"

    def get_objects_by_feature(self, bagid, timestamp, feature):
        traj_features = self.mongo_db["features"]
        timestamp = int(timestamp)

        query_result = traj_features.find(
            {"bag_name": bagid, "timestamp": timestamp})

        if query_result is not None:
            for x in query_result:
                result = x[feature]
        return str(result)

    def get_objects_by_timestamp(self, bagid, timestamp):
        db_traj_data = self.mongo_db["trajectories"]
        timestamp = int(timestamp)

        print("bagid ", bagid, " timestamp", timestamp)

        query_result = db_traj_data.find(
            {"bagid": bagid, "timestamp": timestamp}).distinct("perception_object_id")

        result = []
        if query_result is not None:
            for x in query_result:
                result.append(x)
        return str(result)

    def get_timestamps_by_bagid(self, bagid):
        db_traj_data = self.mongo_db["trajectories"]

        query_result = db_traj_data.find(
            {"bagid": bagid}).distinct("timestamp")

        result = []
        if query_result is not None:
            for x in query_result:
                result.append(x)
        return str(result)

    def get_trajectory_attri(self, bagid, timestamp):
        traj_features = self.mongo_db["features"]
        timestamp = int(timestamp)
        query_result = traj_features.find(
            {"bag_name": bagid, "timestamp": timestamp})
        result = []
        if query_result is not None:
            for x in query_result:
                print("fasdfasfd111")
                result.append(x)
        return str(result)

    def get_trajectory_data(self, bagid, timestamp, objectid, seqlen):
        db_traj_data = self.mongo_db["trajectories"]
        timestamp = int(timestamp)
        objectid = int(objectid)
        seqlen = int(seqlen)
        projection = dict()
        projection['_id'] = 0
        projection['bagid'] = 0
        projection['perception_object_id'] = 0
        projection['timestamp'] = 0
        projection['l'] = 0
        projection['w'] = 0
        projection['h'] = 0
        projection['theta'] = 0
        projection['v_x'] = 0
        projection['v_y'] = 0
        projection['a_x'] = 0
        projection['a_y'] = 0
        projection['lane_id'] = 0
        projection['preception_object_type'] = 0
        projection['is_still'] = 0
        result = []

        query_result = db_traj_data.find(
            {"bagid": bagid, "timestamp": {"$gte": timestamp}, "perception_object_id": objectid}, projection).limit(seqlen)

        if query_result is not None:
            for x in query_result:
                result.append(x)
        return str(result)

    def get_multiple_trajectory_data_by_attribute(self, attribute, seqlen, seqnum):
        logger.info(attribute)
        logger.info(seqlen)
        db_attribute_data = self.mongo_db["features"]
        query_result = db_attribute_data.find(
            {attribute: "true"}).limit(int(seqnum))
        timestamp = -1
        objectid = -1
        bagid = "xxx"
        final_result = []
        db_traj_data = self.mongo_db["trajectories"]
        if query_result is not None:
            for x in query_result:
                logger.info(x)
                timestamp = int(x["timestamp"])
                objectid = int(x["object_id"])
                bagid = x["bag_name"]

                seqlen = int(seqlen)
                projection = dict()
                projection['_id'] = 0
                projection['bagid'] = 0
                projection['perception_object_id'] = 0
                projection['timestamp'] = 0
                projection['l'] = 0
                projection['w'] = 0
                projection['h'] = 0
                projection['theta'] = 0
                projection['v_x'] = 0
                projection['v_y'] = 0
                projection['a_x'] = 0
                projection['a_y'] = 0
                projection['lane_id'] = 0
                projection['preception_object_type'] = 0
                projection['is_still'] = 0
                result = []

                # for i in range(100):
                query_result = db_traj_data.find(
                    {"bagid": bagid, "timestamp": {"$gte": timestamp}, "perception_object_id": objectid}, projection).limit(seqlen)

                if query_result is not None:
                    for x in query_result:
                        logger.info(x)
                        result.append(x)
                    final_result.append(result)
        return str(final_result)

    def get_trajectory_data_by_attribute(self, attribute, seqlen):
        logger.info(attribute)
        logger.info(seqlen)
        db_attribute_data = self.mongo_db["features"]
        query_result = db_attribute_data.find({attribute: "true"}).limit(1)
        timestamp = -1
        objectid = -1
        bagid = "xxx"
        if query_result is not None:
            for x in query_result:
                logger.info(x)
                timestamp = int(x["timestamp"])
                objectid = int(x["object_id"])
                bagid = x["bag_name"]
        db_traj_data = self.mongo_db["trajectories"]

        seqlen = int(seqlen)
        projection = dict()
        projection['_id'] = 0
        projection['bagid'] = 0
        projection['perception_object_id'] = 0
        projection['timestamp'] = 0
        projection['l'] = 0
        projection['w'] = 0
        projection['h'] = 0
        projection['theta'] = 0
        projection['v_x'] = 0
        projection['v_y'] = 0
        projection['a_x'] = 0
        projection['a_y'] = 0
        projection['lane_id'] = 0
        projection['preception_object_type'] = 0
        projection['is_still'] = 0
        result = []

        # for i in range(100):
        query_result = db_traj_data.find(
            {"bagid": bagid, "timestamp": {"$gte": timestamp}, "perception_object_id": objectid}, projection).limit(seqlen)

        if query_result is not None:
            for x in query_result:
                logger.info(x)
                result.append(x)
        return str(result)

    def get_trajectory_data_by_multi_attribute(self, condition, seqlen):
        logger.info(condition)
        logger.info(seqlen)
        db_attribute_data = self.mongo_db["features"]

        query_condition = str(condition)

        query_result = db_attribute_data.find_one(condition)
        timestamp = -1
        objectid = -1
        bagid = " "

        if query_result is not None:
            logger.info(len(list(query_result)))
            logger.info("found one ")
            timestamp = int(query_result["timestamp"])
            objectid = int(query_result["object_id"])
            bagid = query_result["bag_name"]
        else:
            logger.info("not found one")
            return "not found"
        db_traj_data = self.mongo_db["trajectories"]

        seqlen = int(seqlen)
        projection = dict()
        projection['_id'] = 0
        projection['bagid'] = 0
        projection['perception_object_id'] = 0
        projection['timestamp'] = 0
        projection['l'] = 0
        projection['w'] = 0
        projection['h'] = 0
        projection['theta'] = 0
        projection['v_x'] = 0
        projection['v_y'] = 0
        projection['a_x'] = 0
        projection['a_y'] = 0
        projection['lane_id'] = 0
        projection['preception_object_type'] = 0
        projection['is_still'] = 0
        result = []

        # for i in range(100):
        query_result = db_traj_data.find(
            {"bagid": bagid, "timestamp": {"$gte": timestamp}, "perception_object_id": objectid}, projection).limit(seqlen)

        if query_result is not None:
            for x in query_result:
                logger.info(x)
                result.append(x)
        return str(result)

    def get_multi_trajectory_data(self, bagid, start_time, end_time, objectid, seqlen):
        db_traj_data = self.mongo_db["trajectories"]
        start_time = int(start_time)
        end_time = int(end_time)
        objectid = int(objectid)
        seqlen = int(seqlen)
        query_result = db_traj_data.find(
            {"bagid": bagid, "timestamp": {"$gte": start_time, "$lte": end_time}, "perception_object_id": objectid}).limit(seqlen)
        result = []
        if query_result is not None:
            for x in query_result:
                result.append(x)
        return str(result)

    def upload_trajectoryinfo_by_dict(self, data, bagid):
        print("uploading....")
        time_start = time.clock()
        timestart = time.time()
        logger.info("into upload trajectory by dict")

        db_traj_data = self.mongo_db["trajectories"]

        data = json.loads(data)
        traj_data = data["trajectory"]
        # for traj in traj_data:
        #     db_traj_data.update(
        #         {
        #             "bagid": bagid,
        #             "timestamp": traj["timestamp"],
        #             "perception_object_id": obj_id
        #         }, {
        #             "$set": traj
        #         }
        #     )
        logger.info(bagid)
        bulk = db_traj_data.initialize_ordered_bulk_op()
        for traj in traj_data:
            traj["bagid"] = bagid
            bulk.find(
                {
                    "bagid": bagid,
                    "timestamp": traj["timestamp"],
                    "perception_object_id": traj["perception_object_id"]
                }
            ).upsert().update({
                "$set": traj
            })

        timeend1 = time.time()

        bulk.execute()

        timeend2 = time.time()
        logger.info("insert done")
        timecost1 = timeend1 - timestart
        timecost2 = timeend2 - timeend1

        logger.info(timecost1)
        logger.info(timecost2)

    def upload_objectinfo_by_dict(self, data):
        print("uploading....")
        time_start = time.clock()
        timestart = time.time()
        logger.info("into upload object info by dict")

        db_traj_data = self.mongo_db["object_info"]

        data = json.loads(data)
        bulk = db_traj_data.initialize_ordered_bulk_op()
        traj_data = data["trajectory"]
        for traj in traj_data:
            bulk.find(
                {
                    "bagId": traj["bagId"],
                    "perception_object_id": traj["perception_object_id"]
                }
            ).upsert().update({
                "$set": traj
            })

        timeend1 = time.time()
        bulk.execute()
        timeend2 = time.time()
        logger.info("insert done")
        timecost1 = timeend1 - timestart
        timecost2 = timeend2 - timeend1

        logger.info(timecost1)
        logger.info(timecost2)

    def upload_baginfo_by_dict(self, data):
        print("uploading....")
        time_start = time.clock()
        timestart = time.time()
        logger.info("into upload bag info by dict")

        db_traj_data = self.mongo_db["bag_info"]

        data = json.loads(data)
        bulk = db_traj_data.initialize_ordered_bulk_op()

        bulk.find(
            {
                "bagId": data["bagId"]
            }
        ).upsert().update({
            "$set": data
        })

        timeend1 = time.time()
        bulk.execute()
        timeend2 = time.time()
        logger.info("insert done")
        timecost1 = timeend1 - timestart
        timecost2 = timeend2 - timeend1

        logger.info(timecost1)
        logger.info(timecost2)

    def upload_trajectoryinfo_by_id(self, data, bagid):
        print("uploading....")
        result = {}
        db_traj_data = self.mongo_db["trajectories"]

        prediction_objects = PredictionObstacles()
        prediction_objects.ParseFromString(
            base64.b64decode(data.encode('utf-8')))

        timestamp = prediction_objects.time_measurement
        for prediction_object in prediction_objects.prediction_obstacle:
            perception_object = prediction_object.perception_obstacle
            lane = prediction_object.feature[0].lane
            is_still = prediction_object.feature[0].is_still
            if len(lane.current_lane_feature) > 0:
                lane_id = lane.current_lane_feature[0].lane_id
            else:
                lane_id = -1
            result[perception_object.id] = []
            data_dict = {}
            x, y, z = perception_object.position.x, perception_object.position.y, perception_object.position.z
            l, w, h = perception_object.length, perception_object.width, perception_object.height
            theta = perception_object.theta
            v_x, v_y = perception_object.velocity.x, perception_object.velocity.y
            a_x, a_y = perception_object.acceleration.x, perception_object.acceleration.y
            need_fields = [timestamp, x, y, z, l, w, h, theta, v_x, v_y, a_x, a_y,
                           lane_id, perception_object.type, is_still]

            result[perception_object.id].append(need_fields)
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
        # print("before evaluate")
        # self.evaluate_trajectories(bagid, seqlen)
        # print("upload done")
        return result

    def upload_attri_by_id(self, data, bag_name):
        print("upload attribute 111....")
        db_attri_data = self.mongo_db["features"]
        data = json.loads(data)
        logger.info("upload attribute")
        bulk = db_attri_data.initialize_ordered_bulk_op()
        for attri_per_time in data:
            attri_data = attri_per_time["attribute"]
            for attri in attri_data:
                attri["bag_name"] = bag_name
                attri["timestamp"] = attri_per_time["timestamp"]
                bulk.find(
                    {
                        "bag_name": bag_name,
                        "timestamp": attri_per_time["timestamp"],
                        "object_id": attri["object_id"]
                    }
                ).upsert().update({
                    "$set": attri
                })

        bulk.execute()

        logger.info("upload attribute done")
        print("done upload")
        return "done"

# labeling related

    def get_labeling_time_by_id(self, bagid):
        result = ""
        db_label_data = self.mongo_db["labeling_time"]
        query_result = db_label_data.find(
            {"bagId": bagid}, {"_id": 0})

        if query_result is not None:
            for x in query_result:
                result = x
        return str(result)

    def upload_labeling_time_by_id(self, data, bagid):
        print("upload labeling time 111....")
        result = {}
        db_label_data = self.mongo_db["labeling_time"]
        insert_data = dict()
        insert_data["data"] = data
        db_label_data.update(
            {
                "bagId": bagid
            }, {
                "$set": insert_data
            }, True
        )
        print("done insert")
        return "done"

    def get_labeling_index_by_id(self, bagid, topic):
        result = ""
        db_label_data = self.mongo_db["labeling_index"]
        query_result = db_label_data.find(
            {"bagId": bagid, "topic": topic}, {"_id": 0})

        if query_result is not None:
            for x in query_result:
                result = x
        return str(result)

    def upload_labeling_index_by_id(self, data, bagid):
        print("upload labeling 111....")
        result = {}
        db_label_data = self.mongo_db["labeling_index"]

        data = json.loads(data)

        for key in data.keys():
            insert_data = dict()
            insert_data["topic"] = key
            insert_data["bagId"] = bagid
            insert_data["data"] = data[key]
            db_label_data.update(
                {
                    "topic": key,
                    "bagId": bagid
                }, {
                    "$set": insert_data
                }, True
            )
        print("done insert")
        return "done"

    def upload_labeling_data_init(self, data):
        print("upload labeling time 111....")
        result = {}

        data_dict = data
        db_label_data = self.mongo_db["labeling_data"]

        frame_field = data_dict["frameFields"]
        insert_data = dict()
        insert_data[frame_field] = data_dict["data"]

        db_label_data.update(
            {
                "timestamp": data_dict["timestamp"],
                "index": data_dict["frameId"],
                "bagid": data_dict["bagId"]
            }, {
                "$set": insert_data
            }, True
        )

        print("done insert")
        return "done"

    def upload_labeling_data(self, data):
        print("upload labeling time 111....")
        result = {}

        data_dict = data
        db_label_data = self.mongo_db["labeling_data"]

        frame_field = data_dict["frameFields"]
        insert_data = dict()
        insert_data[frame_field] = data_dict["data"]

        print("insert data")
        if data_dict["timestamp"] == "0":
            db_label_data.update(
                {
                    "index": data_dict["frameId"],
                    "bagid": data_dict["bagId"]
                }, {
                    "$set": insert_data
                }, True
            )
        else:
            db_label_data.update(
                {
                    "timestamp": data_dict["timestamp"],
                    "bagid": data_dict["bagId"]
                }, {
                    "$set": insert_data
                }, True
            )

        print("done insert")
        return "done"

    def get_labeling_data(self, bagid,  anotation_type, frame_index):
        result = []
        db_label_data = self.mongo_db["labeling_data"]
        query_result = db_label_data.find(
            {"bagid": bagid, "index": frame_index, "anotation": anotation_type})

        if query_result is not None:
            for x in query_result:
                result.append(x)
        return str(result)

    def get_labeling_data_by_post(self, data_dict):
        print("into get labeling  @@@@@@")
        result = []
        db_label_data = self.mongo_db["labeling_data"]

        frame_fields = data_dict.getlist("frameFields")

        projection = dict()
        for i, field in enumerate(frame_fields):
            projection[field] = 1
        projection['_id'] = 0
        query_result = {}
        data_dict = data_dict.dict()
        if data_dict["timestamp"] == '0':
            query_result = db_label_data.find(
                {"bagid": data_dict["bagId"], "index": data_dict["frameId"]}, projection)
        else:
            query_result = db_label_data.find(
                {"bagid": data_dict["bagId"], "timestamp": data_dict["timestamp"]}, projection)
        if query_result is not None:
            for x in query_result:
                result.append(x)
        return str(result)

    def get_multi_labelinginfo_by_id(self, bagid, start, end):
        result = []
        db_label_data = self.mongo_db["labelings"]
        query_result = db_label_data.find(
            {"bagid": bagid, "index": {"$gte": start, "$lte": end}})

        if query_result is not None:
            for x in query_result:
                result.append(x)
        return str(result)

    def consistency_check(self, bagid):
        print(bagid)
        db_traj_data = self.mongo_db["trajectories"]
        myCursor = db_traj_data.distinct({"timestamp"})
        count = 0
        for record in myCursor:
            count += 1
        return str(count)
