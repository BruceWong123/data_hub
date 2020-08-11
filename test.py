#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import json
import time
import rosbag
from pymongo import MongoClient
import six.moves.urllib as urllib


class RosbagParser(object):
    def __init__(self, bag):
        self.topic_list = ["/perception/objects"]
        self.bag = bag

    def connect_to_db(self):
        username = urllib.parse.quote_plus('deep')
        password = urllib.parse.quote_plus('route')
        self.myclient = MongoClient(
            'mongodb://%s:%s@34.218.26.149/datahub' % (username, password))
        self.mydb = self.myclient["datahub"]
        print(self.myclient.list_database_names())

    def insert_frame_data_to_db(self):
        col = self.mydb["messages"]
        start_time_s = time.time()
        data_list = []
        with rosbag.Bag(self.bag) as bag:
            for topic, msg, t in bag.read_messages(topics=self.topic_list):
                data = {"bagid": self.bag, "timestamp": str(
                    t), "topic": "ddd", "message": str(222)}
                data_list.append(data)
                break
        col.insert_many(data_list)
        print (len(data_list))
        end_time_s = time.time()
        print ("Insert time elapsed: ", end_time_s - start_time_s)

    def get_data_from_db(self):
        col = self.mydb["messages"]
        start_time = time.time()
        result = col.find({"topic": {"$regex": "^/p"}})
        print("--- %s seconds --- for reading " % (time.time() - start_time))
        for x in result:
            tt = x.get('timestamp')
            print (tt)
            y = col.find_one(
                {"$and": [{"topic": {"$regex": "^/p"}}, {"timestamp": {"$lt": tt}}]}, sort=[("timestamp", -1)])
            print(" perception timestamp: ", x.get('timestamp'),
                  " carstate timestamp: ", y.get('timestamp'))


if __name__ == "__main__":
    bag_path = '/home/proz023/work/bags/bbb.bag'
    rp = RosbagParser(bag_path)
    rp.connect_to_db()
    rp.insert_frame_data_to_db()
    rp.get_data_from_db()
