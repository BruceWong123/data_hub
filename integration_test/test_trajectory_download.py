import requests
from pathlib import Path
import os
import json
from pymongo import MongoClient

import requests
import base64


class Test_trajectory_download:
    def __init__(self):
        pass

    def test_download_trajectory_data_multiattributes(self, query_dict):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/data/multiattributes/download/"
        session = requests.session()
        session.keep_alive = False
        result = session.put(url=upload_url, data=query_dict)
        return result.text

    def test_download_trajectory_data(self, attribute, seqlen):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/data/" + \
            attribute + "/" + str(seqlen) + "/"

        session = requests.session()
        session.keep_alive = False
        result = session.get(url=upload_url)
        return result.text

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
