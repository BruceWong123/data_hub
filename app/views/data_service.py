import time
import json
import threading
import asyncio
import re
import requests
import os.path as osp
from collections import OrderedDict
import yaml
import websockets
from app.views.deeproute_perception_obstacle_pb2 import PerceptionObstacles


async def get_topic_data_in_frames(ws_url, token, result):

    print("get topic from datapipeline")
    async with websockets.connect(ws_url, max_size=2 ** 32) as websocket:
        handshake = dict()
        handshake['type'] = 'handshake'
        handshake['token'] = token
        await websocket.send(json.dumps(handshake))
        handshake_response = await websocket.recv()
        hs_res = eval(handshake_response)
        if hs_res['sessionStatus'] == 'Open':
            print("send out request")
            render_topic = dict()
            render_topic['type'] = 'timeline_index'
            render_topic['dataId'] = 'YR_MKZ_1_20210122_060128.bag'
            render_topic['topic'] = '/perception/objects'
            render_topic['startTime'] = '1584369292801341'
            render_topic['endTime'] = '1584369293801341'

            try:
                await websocket.send(json.dumps(render_topic))
                start = time.time()
                topic_response = await websocket.recv()
                print('Time:', time.time() - start)
                frame_pattern = r'"binaryOffsetEnd":([0-9]*),"binaryOffsetStart":([0-9]*)'
                frames = re.findall(frame_pattern, topic_response)
                print(frames)
                print(topic_response)
                # receive binary data
                binary_data = await websocket.recv()
                perception_object = PerceptionObstacles()
                for frame in frames:
                    perception_object.ParseFromString(
                        binary_data[int(frame[1])+4:int(frame[0])+1])
                    result.append(perception_object)
            except Exception as ex:
                print("Got binary data error, Exception: %s" % ex)

        else:
            print('RESPONSE:', hs_res)


def get_token():
    """ Get token by username and password

    Args::
        config (dict): data pipeline configuration
    """
    url = 'http://data.dev.deeproute.ai:8091/api/user/login'
    data = {'username': 'perceptionteam',
            'password': 'r6zR86V4*+=*'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    token_pattern = r'[a-z0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}'
    reg = re.compile(token_pattern)
    token = reg.search(response.text).group(0)
    return token


def parse_single_frame():
    url = 'ws://10.10.10.70:8088/data/provider/ws/data/rosbag/binary'
    token = get_token()
    loop = asyncio.new_event_loop()
    binary_data = []
    asyncio.set_event_loop(loop)
    loop.run_until_complete(get_topic_data_in_frames(url, token, binary_data))
    loop.close()
    print("loop closed")
    return binary_data
