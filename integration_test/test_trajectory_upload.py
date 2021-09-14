import base64

import requests
from pathlib import Path
import os
import json
from pymongo import MongoClient
import sys

import os
import pickle
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
sys.path.append(parentUrl)


class Test_trajectory_upload:
    def __init__(self):
        pass

    def test_upload_attributes(self):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/attributes/upload/"

        data = "{\"bag_name\": \"YR_MKZ_1_20201207_022851_755_40\", \"timestamp\": \"1580604436850000\", \"object_id\": \"32663\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}"
        data_dict = {}
        data_dict["data"] = data
        session = requests.session()
        session.keep_alive = False
        print(data_dict)
        session.put(url=upload_url, data=data_dict)
        print("upload done")

    def test_upload_attributes_by_file(self, sample_num):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/attributes/upload/"

        # data = "{\"bag_name\": \"YR_MKZ_1_20201207_022851_755_40\", \"timestamp\": \"1580604436850000\", \"object_id\": \"32663\", \"turn\": \"false\", \"is_still\": \"true\", \"on_lane\": \"false\", \"lane_change\": \"true\", \"on_crosswalk\": \"true\", \"in_junction\": \"false\"}"

        raw_data = self.load_data_from_file("attribute_test_file.pkl")

        # with open('attribute_output.txt', 'w') as f:
        #     print(attribute_data, file=f)

        attribute_data = raw_data["data"]
        attri_list = json.loads(attribute_data)
        first_n = attri_list[0:sample_num]
        attri_json = json.dumps(first_n)

        data_dict = {}
        data_dict["data"] = attri_json
        data_dict["bagId"] = raw_data["bagId"]
        session = requests.session()
        session.keep_alive = False

        session.put(url=upload_url, data=data_dict)

    def test_upload_trajectory(self, filename):
        # service_end_point = "http://127.0.0.1:8000/api/"
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/upload/"

        data = ""
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                data += " "
                data += line

        data_dict = {}
        data_dict["data"] = data
        data_dict["bagid"] = "YR_MKZ_1_20201207_022851_755_40"
        session = requests.session()
        session.keep_alive = False
        # print(data)
        session.put(url=upload_url, data=data_dict)
        print("download done")

    def test_upload_trajectory_by_dict(self):
        print("into upload by dict")
        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/upload/"

        data = "{\"trajectory\": [{\"perception_object_id\": \"1111\", \"timestamp\": \"2323232\", \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}, {\"perception_object_id\": \"262433\", \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"},{\"perception_object_id\": \"262633\", \"timestamp\": \"2323232\",      \"perception_obj_type\": \"xxx\",\"x\": \"1111\",\"y\": \"2222\",\"z\": \"3333\",\"l\": \"333\",   \"w\": \"333\",\"h\": \"45\",\"theta\": \"1111\",\"v_x\": \"2222\",\"v_y\": \"3333\",\"a_x\": \"333\",\"a_y\": \"333\",\"is_still\": \"false\",\"lane_s\": \"1111\",\"lane_l\": \"2222\",      \"dist_to_left_boundary\": \"3333\",\"dist_to_right_boundary\": \"3333\",\"lane_sequences\": \"3333\"}]}"

        data_dict = {}
        data_dict["data"] = data
        data_dict["bagId"] = "test_test_test_test_test"
        session = requests.session()
        session.keep_alive = False
        session.put(url=upload_url, data=data_dict)
        print("upload done")

    def load_data_from_file(self, file_name):

        with (open(file_name, "rb")) as openfile:
            while True:
                try:
                    return pickle.load(openfile)
                except EOFError:
                    break
        return None

    def test_upload_trajectory_by_file(self, traj_num):

        service_end_point = "http://dataserver.prediction.simulation.deeproute.ai/api/"
        upload_url = service_end_point + "trajectory/upload/"

        raw_data = self.load_data_from_file(
            "trajectory_test_file.pkl")

        # with open('traj_output.txt', 'w') as f:
        #     print(pkl_data, file=f)

        trajectory_data = raw_data["data"]

        # traj_json = json.loads(trajectory_data)
        # traj_list = traj_json["trajectory"]
        # upload_list = traj_list[0:traj_num]

        bagId = raw_data["bagId"]
        trajectory_data = raw_data["data"]
        traj_data = json.loads(trajectory_data)

        traj_list = traj_data["trajectory"]
        first_n = traj_list[0:traj_num]
        traj_json = json.dumps(first_n)

        # print(traj_json)
        traj_dict = "{\"trajectory\":" + traj_json + "}"

        # print(traj_dict)
        data_dict = {}
        data_dict["data"] = traj_dict
        data_dict["bagId"] = bagId
        session = requests.session()
        session.keep_alive = False
        # print(data)
        session.put(url=upload_url, data=data_dict)

    def upload_by_file(self):
        file_path = '/home/bruce/datahub/bag_'

        for iroot, idirs, ifiles in os.walk(file_path):
            for f in ifiles:
                filename = os.path.join(iroot, f)
                print(filename)
                self.upload_trajectory(filename)
                print("parse done!")

        # filename = '/home/bruce/datahub/data_hub/app/views/predictionData.txt'
        # upload_trajectory(filename)

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
