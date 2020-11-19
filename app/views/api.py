from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Bag
from ..serializers import *
from app.views.db_manager import DBManager
import json
import logging
logger = logging.getLogger(__name__)


db = DBManager()


@ api_view(['GET', 'PUT', 'DELETE'])
def getAllTimestampsByID(request, bagid):
    if request.method == 'GET':
        return HttpResponse(db.get_all_timestamps_by_id(bagid))


@ api_view(['GET', 'PUT', 'DELETE'])
def getFrameByIdTime(request, bagid, timestamp):
    if request.method == 'GET':
        return HttpResponse(db.get_frame_by_id_time(bagid, timestamp))


@ api_view(['GET', 'PUT', 'DELETE'])
def getMessageByIdTimeTopic(request, bagid, timestamp, topic):
    if request.method == 'GET':
        return HttpResponse(db.get_message_by_id_time_topic(bagid, timestamp, topic))


@ api_view(['GET', 'POST', 'DELETE'])
def uploadMessageByIdTimeTopic(request, bagid, timestamp, topic):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_message_by_id_topic(
                data_dict, bagid, timestamp, topic)


@ api_view(['GET', 'PUT', 'DELETE'])
def getRangeMessageByIdTopic(request, bagid, topic, start, end):
    if request.method == 'GET':
        return HttpResponse(db.get_range_message_by_id_topic(bagid, topic, start, end))

# task related


@ api_view(['GET', 'POST', 'DELETE'])
def uploadTaskInfo(request, taskid, play_mode, scene_id, subscene_id, planning_version, perception_version):
    if request.method == 'POST':
        db.upload_task_info(
            taskid, play_mode, scene_id, subscene_id, planning_version, perception_version)


@ api_view(['GET', 'PUT', 'DELETE'])
def getTaskInfoById(request, taskid):
    if request.method == 'GET':
        return JsonResponse(db.get_taskinfo_by_id(taskid))


# task/frame result related
@ api_view(['POST'])
def uploadBagResultByIDVersionMode(request, taskid, grading_version, play_mode):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_task_result_by_id_version_mode(
                data_dict, taskid, grading_version, play_mode)


@ api_view(['POST'])
def uploadFrameResultByIDVersionTime(request, taskid, grading_version, timestamp):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_task_frame_result_by_id_version_mode(
                data_dict, taskid, grading_version, timestamp)


@ api_view(['GET'])
def getBagResultByIDVersionMode(request, taskid, grading_version, play_mode):
    if request.method == 'GET':
        result_str = db.get_task_result_by_id_version_mode(
            taskid, grading_version, play_mode)
        return JsonResponse({'result': result_str})


@ api_view(['GET'])
def getFrameResultByIDVersionTime(request, taskid, grading_version, timestamp):
    if request.method == 'GET':
        result_str = db.get_task_frame_result_by_id_version_mode(
            taskid, grading_version, timestamp)
        return JsonResponse({'debug_info': result_str})
