import requests
from pathlib import Path
import os


class Test_UPload:
    def __init__(self):
        print("init")
        pass

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
    test.upload_by_file()
