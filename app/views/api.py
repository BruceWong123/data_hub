
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
from django.http import QueryDict

logger = logging.getLogger('django')

db = DBManager()


@ api_view(['GET', 'PUT', 'DELETE'])
def getAllBagID(request):
    if request.method == 'GET':
        logger.info("########### get all bag id ##################")
        session_key = request.session.session_key
        logger.info("session id: ")
        logger.info(session_key)
        return HttpResponse(db.get_all_bag_id())


# Trajectory related
@ api_view(['GET', 'PUT', 'DELETE'])
def getTrajectoryInfoById(request, bagid):
    if request.method == 'GET':
        return JsonResponse(db.get_trajectoryinfo_by_id(bagid))

# Trajectory related


@ api_view(['GET', 'PUT', 'DELETE'])
def getTrajectoryAttri(request, bagid, timestamp):
    if request.method == 'GET':
        print("get attributes")
        return JsonResponse({'result': db.get_trajectory_attri(bagid, timestamp)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getTrajectoryData(request, bagid, timestamp, objectid, seqlen):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_trajectory_data(bagid, timestamp, objectid, seqlen)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getTrajectoryDataByMultiAttribute(request):
    if request.method == 'PUT':
        return JsonResponse({'result': db.get_trajectory_data_by_multi_attribute(request.data.dict(), 50)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getTrajectoryDataByAttribute(request, attribute, seqlen):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_trajectory_data_by_attribute(attribute, seqlen)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getMultipleTrajectoryDataByAttribute(request, attribute, seqlen, seqnum):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_multiple_trajectory_data_by_attribute(attribute, seqlen, seqnum)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getMultiTrajectoryData(request, bagid, start_time, end_time, objectid, seqlen):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_multi_trajectory_data(bagid, start_time, end_time, objectid, seqlen)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getObjectsByFeature(request, bagid, timestamp, feature):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_objects_by_feature(bagid, timestamp, feature)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getObjectsByTimestamp(request, bagid, timestamp):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_objects_by_timestamp(bagid, timestamp)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getBagidsInTrajectory(request):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_all_bagids_trajectory()})


@ api_view(['GET', 'PUT', 'DELETE'])
def getTimestampsByBagid(request, bagid):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_timestamps_by_bagid(bagid)})


@ api_view(['GET', 'PUT', 'DELETE'])
def evaluateTrajectoryById(request, bagid):
    if request.method == 'GET':
        return JsonResponse({'result': db.evaluate_trajectories(bagid, 50)})


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadTrajectoryInfoByDict(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        print("into put")
        logger.info("in trajectory by dict")
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_trajectoryinfo_by_dict(request_dict.get("data"), request_dict.get("bagId")), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadObjectInfoByDict(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        print("into put")
        logger.info("in object by dict")
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_objectinfo_by_dict(request_dict.get("data")), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadBagInfoByDict(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        print("into put")
        logger.info("in bag by dict")
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_baginfo_by_dict(request_dict.get("data")), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadTrajectoryInfoById(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        print("into put")
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_trajectoryinfo_by_id(request_dict.get("data"), request_dict.get("bagid")), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadTrajectoryAttri(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_attri_by_id(request_dict.get("data"), request_dict.get("bagId")), safe=False)


# labeling related


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadLabelingIndexById(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_labeling_index_by_id(request_dict.get("data"), request_dict.get("bagId")), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadLabelingData(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        data_dict = request.data.dict()
        return JsonResponse(db.upload_labeling_data(data_dict), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadLabelingDataInit(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        data_dict = request.data.dict()
        return JsonResponse(db.upload_labeling_data_init(data_dict), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def getLabelingIndexById(request, bagid, topic):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_labeling_index_by_id(bagid, topic)})


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadLabelingTimeById(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_labeling_time_by_id(request_dict.get("data"), request_dict.get("bagId")), safe=False)


@ api_view(['GET', 'PUT', 'DELETE'])
def getLabelingTimeById(request, bagid):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_labeling_time_by_id(bagid)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getLabelingData(request, bagid, anotation_type, frame_index):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_labeling_data(bagid, anotation_type, frame_index)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getLabelingDataByPost(request):
    if request.method == 'PUT':

        if request.data is not None:
            print("into get labeling data")
            print(request.data.dict())
            return JsonResponse({'result': db.get_labeling_data_by_post(request.data)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getMultiLabelingInfoById(request, bagid, start, end):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_multi_labelinginfo_by_id(bagid, start, end)})


@ api_view(['GET', 'PUT', 'DELETE'])
def consistencyCheck(request, bagid):
    print("into api ")
    return JsonResponse({'result': db.consistency_check(bagid)})
