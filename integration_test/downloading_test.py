import requests
from pathlib import Path
import os
import json
from pymongo import MongoClient

import labeling.perception_labeling_rosbag_parser_pb2 as perception_labeling

from celery import Celery
import requests
import base64


class Downloading_test:
    def __init__(self):
        print("init")
        pass

    def download_labeling_data(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "labeling/data/download/"

        data_dict = dict()
        data_dict["bagId"] = "YR_MKZ_1_20210105_biandao_PM2"
        data_dict["frameId"] = 0
        data_dict["timestamp"] = "0"
        frame_fields = []
        frame_fields.append("object_3d")
        data_dict["frameFields"] = frame_fields

        session = requests.session()
        session.keep_alive = False
        result = session.put(url=upload_url, data=data_dict)
        print(result)

    def download_trajectory_data(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/data/is_still/50/"

        session = requests.session()
        session.keep_alive = False
        result = session.get(url=upload_url)
        print(result)

    def test_mongo(self):
        host = '43.130.32.126'
        port = 27017
        authSource = "tw"
        print("connecting db")
        self.my_mongo_client = MongoClient(
            "mongodb://%s:%s@%s:%s/%s" % ('bruce',
                                          'twitter', host, port, 'tw')
        )
        self.mongo_db = self.my_mongo_client["tw"]
        print(
            "Successfully connected to Mongo"
        )

        db_users = self.mongo_db["users"]
        query_result = db_users.find({"tst": "test"})
        for x in query_result:
            print(x)
