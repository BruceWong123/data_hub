import requests
from pathlib import Path
import os
import json
from pymongo import MongoClient

import requests
import base64


class Test_labeling_download:
    def __init__(self):
        pass

    def test_downloading_labeling_data(selt):
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
        return result.text
