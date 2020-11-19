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
def getFrameByIdTime(request, bagid, time):
    if request.method == 'GET':
        return HttpResponse(db.get_frame_by_id_time(bagid, time))


@ api_view(['GET', 'PUT', 'DELETE'])
def getMessageByIdTimeTopic(request, bagid, time, topic):
    if request.method == 'GET':
        return HttpResponse(db.get_message_by_id_time_topic(bagid, time, topic))


@ api_view(['GET', 'PUT', 'DELETE'])
def getRangeMessageByIdTopic(request, bagid, topic, start, end):
    if request.method == 'GET':
        return HttpResponse(db.get_range_message_by_id_topic(bagid, topic, start, end))


@ api_view(['POST'])
def uploadBagResultByIDVersionMode(request, bagid, function_version, grading_version, play_mode):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_bag_result_by_id_version_mode(
                data_dict, bagid, function_version, grading_version, play_mode)


@ api_view(['POST'])
def uploadFrameResultByIDVersionTime(request, bagid, function_version, grading_version, timestamp):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_frame_result_by_id_version_mode(
                data_dict, bagid, function_version, grading_version, timestamp)


@ api_view(['GET'])
def getBagResultByIDVersionMode(request, bagid, function_version, grading_version, play_mode):
    if request.method == 'GET':
        result_str = db.get_bag_result_by_id_version_mode(
            bagid, function_version, grading_version, play_mode)
        return JsonResponse({'result': result_str})


@ api_view(['GET'])
def getFrameResultByIDVersionTime(request, bagid, function_version, grading_version, timestamp):
    if request.method == 'GET':
        result_str = db.get_frame_result_by_id_version_mode(
            bagid, function_version, grading_version, timestamp)
        return JsonResponse({'debug_info': result_str})
