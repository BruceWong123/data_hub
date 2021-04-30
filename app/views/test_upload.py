import requests
from pathlib import Path
import os
import json


class Test_UPload:
    def __init__(self):
        print("init")
        pass

    def upload_labeling(self):
        service_end_point = "http://127.0.0.1:8000/api/"
        upload_url = service_end_point + "labeling/upload/"

        data = "{\"8\": {\"timestamp\": {\"objects\": 1584360195850000, \"camera6\": 1584360195883748838, \"camera2\": 1584360195916826862, \"camera1\": 1584360195900073653}, \"rostime\": {\"objects\": \"1584360196018079\", \"camera6\": \"1584360195903940\", \"camera2\": \"1584360195939053\", \"camera1\": \"1584360195922630\"}}, \"9\": {\"timestamp\": {\"objects\": 1584360195950000, \"camera6\": 1584360195983747510, \"camera2\": 1584360196016829070, \"camera1\": 1584360196000116133}, \"rostime\": {\"objects\": \"1584360196117999\", \"camera6\": \"1584360196004368\", \"camera2\": \"1584360196038858\", \"camera1\": \"1584360196023211\"}}}"
        # data = json.loads(data)

        data_dict = {}
        data_dict["data"] = data
        data_dict["bagid"] = "YR_MKZ_1_20201207_022851_755_40"
        session = requests.session()
        session.keep_alive = False
        print(data_dict)
        session.put(url=upload_url, data=data_dict)
        print("upload done")

    def upload_attributes(self):
        service_end_point = "http://127.0.0.1:8000/api/"
        upload_url = service_end_point + "trajectory/attributes/upload/"

        data = "{ \"1580604434350000\":{\"bag_name\": \"YR_MKZ_1_20201207_022851_755_40\", \"timestamp\": 1580604434350000, \"ids\": [], \"turn\": [], \"is_still\": [1], \"on_lane\": [1], \"lane_change\": [], \"on_crosswalk\": [], \"in_junction\": []}}"

        data_dict = {}
        data_dict["bagid"] = "YR_MKZ_1_20201207_022851_755_40"
        data_dict["data"] = data
        session = requests.session()
        session.keep_alive = False
        print(data_dict)
        session.put(url=upload_url, data=data_dict)
        print("upload done")

    def upload_trajectory(self, filename):
        service_end_point = "http://127.0.0.1:8000/api/"
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
        print("upload done")

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


if __name__ == '__main__':
    test = Test_UPload()
    test.upload_attributes()
