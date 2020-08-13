import os
import json
import time
import rosbag
from pymongo import MongoClient
import six.moves.urllib as urllib
import mysql.connector as mysql
from datetime import datetime


class RosbagParser(object):
    def __init__(self, bag):
        self.topic_list = ["/perception/objects"]
        self.bag = bag

    def connect_to_mongodb(self):
        username = urllib.parse.quote_plus('deep')
        password = urllib.parse.quote_plus('route')
        self.myclient = MongoClient(
            'mongodb://%s:%s@34.218.26.149/datahub' % (username, password))
        self.db_mongo = self.myclient["datahub"]
        print("Successfully connected to Mongo : %s" %
              self.myclient.list_database_names())

    def connect_to_mysql(self):
        HOST = "34.218.26.149"
        DATABASE = "data_hub"
        USER = "deeproute"
        PASSWORD = "deeproute"
        self.db_mysql = mysql.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD)
        print("Successfully Connected to remote MySQL : %s" %
              self.db_mysql.get_server_info())

    def insert_bag_into_to_mysql(self):
        mycursor = self.db_mysql.cursor()
        bag_id = "fremont_1"
        now = datetime.now()
        bag_date = now.strftime('%Y-%m-%d %H:%M:%S')

        sql = "INSERT INTO app_bag (country, city, location, uploader, vehicle, description, date, status, start, end, bagid) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        val = ("US", "Fremont", "small loop", "Yajun Wang", "MKZ01",
               "small loop near us site", bag_date, "uploading", "0", "2583635907918130067", bag_id)
        mycursor.execute(sql, val)

        self.db_mysql.commit()

        print("Successfully inserted to remote MySQL with bag id: % s" % bag_id)
        return bag_id

    def insert_frame_data_to_mongodb(self):
        col = self.db_mongo["messages"]
        start_time_s = time.time()
        bag_id = self.insert_bag_into_to_mysql()
        data_list = []

        with rosbag.Bag(self.bag) as bag:
            for topic, msg, t in bag.read_messages():
                data = {"bagid": bag_id, "timestamp": str(
                    t), "topic": str(topic), "message": str(msg)}
                data_list.append(data)
                print("insert one row")
        col.insert_many(data_list)
        print (len(data_list))
        end_time_s = time.time()
        print ("Insert time elapsed: ", end_time_s - start_time_s)

    def get_data_from_db(self):
        col = self.db_mongo["messages"]
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
    bag_path = '/home/bruce/bags/bag3.bag'
    rp = RosbagParser(bag_path)
    rp.connect_to_mongodb()
    rp.connect_to_mysql()
    rp.insert_frame_data_to_mongodb()
    # rp.get_data_from_db()
