import os
import sys
import time
import base64
import zlib
import pprint
import requests
import configparser
from pymongo import MongoClient
import six.moves.urllib as urllib
import mysql.connector as mysql
from datetime import datetime


class DBManager(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.abspath(
            os.path.dirname(__file__)) + "/config.ini")
        self.connect_to_mongodb()
        self.connect_to_mysql()

    def connect_to_mongodb(self):
        host = self.config.get("MongoDB", "host")
        port = self.config.get("MongoDB", "port")
        database = self.config.get("MongoDB", "database")
        username = urllib.parse.quote_plus(self.config.get("MongoDB", "user"))
        password = urllib.parse.quote_plus(
            self.config.get("MongoDB", "password"))

        self.my_mongo_client = MongoClient(
            "mongodb://%s:%s@%s:%s/%s" % (username,
                                          password, host, port, database)
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

    def translateTopic(self, topic):
        if topic == 'perception':
            return '/perception/objects'
        elif topic == 'carstate':
            return '/canbus/car_state'
        elif topic == 'signals_response':
            return '/perception/signals_response'
        elif topic == 'context':
            return '/planner/context'
        elif topic == 'debug_info':
            return '/planner/debug_info'

    def get_all_timestamps_by_id(self, bagid):
        result = ""
        self.connect_to_mysql()
        sql = "SELECT association FROM app_association WHERE bagid = %s"
        adr = (bagid, )
        self.mysql_cursor.execute(sql, adr)
        query_result = self.mysql_cursor.fetchall()
        for row in query_result:
            result += " "
            result += str(row[0])
        self.close_mysql()
        return result

    def get_frame_by_id_time(self, bagid, time):
        result = "no data found"
        db_messages = self.mongo_db["messages"]
        query_result = db_messages.find({"bagid": bagid, "timestamp": {"$lte": time}, "topic": {
            "$regex": "^/perception/objects"}})
        for x in query_result:
            y = db_messages.find_one({"$and": [{"bagid": bagid, "topic": {
                "$regex": "^/canbus/car_state"}}, {"timestamp": {"$lte": time}}]}, sort=[("timestamp", -1)])
            if not y:
                break
            result = y.get('message') + " | " + x["message"]
        return result

    def get_message_by_id_time_topic(self, bagid, time, topic):
        result = " "
        db_messages = self.mongo_db["messages"]
        topic = self.translateTopic(topic)
        query_result = db_messages.find(
            {"bagid": bagid, "timestamp": time, "topic": topic})
        for x in query_result:
            result = x['message']
        return result

    def get_range_message_by_id_topic(self, bagid, topic, start, end):
        result = ""
        topic = self.translateTopic(topic)
        db_messages = self.mongo_db["messages"]
        query_result = db_messages.find(
            {"bagid": bagid, "timestamp": {'$lte': end, '$gte': start}, "topic": topic}).sort("timestamp")
        for i, x in enumerate(query_result):
            result += x['message']
            if i != query_result.count() - 1:
                result += "deep_route"
        return result

    def upload_bag_result_by_id_version_mode(self, data_dict, bagid, function_version, grading_version, play_mode):
        db_bag_results = self.mongo_db["bag_results"]
        query_result = db_bag_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "play_mode": play_mode})

        if query_result is None:
            metadata_dict = {
                "bagid": bagid,
                "function_version": function_version,
                "grading_version": grading_version,
                "play_mode": play_mode
            }
            db_bag_results.insert_one({**metadata_dict, **data_dict})

        else:
            db_bag_results.update(
                {
                    "_id": query_result.get('_id')
                }, {
                    "$set": data_dict
                }
            )

    def get_bag_result_by_id_version_mode(self, bagid, function_version, grading_version, play_mode):
        result = ""
        db_bag_results = self.mongo_db["bag_results"]
        query_result = db_bag_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "play_mode": play_mode})
        if query_result is not None:
            result = query_result.get('result')
        return result

    def upload_frame_result_by_id_version_mode(self, data_dict, bagid, function_version, grading_version, timestamp):
        db_frame_results = self.mongo_db["frame_results"]
        query_result = db_frame_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "timestamp": timestamp})

        if query_result is None:
            metadata_dict = {
                "bagid": bagid,
                "function_version": function_version,
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

    def get_frame_result_by_id_version_mode(self, bagid, function_version, grading_version, timestamp):
        db_frame_results = self.mongo_db["frame_results"]
        result = ""
        query_result = db_frame_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "timestamp": timestamp})
        if query_result is not None:
            result = query_result.get('debug_info')
        return result
