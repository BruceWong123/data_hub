
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


@ api_view(['GET', 'PUT', 'DELETE'])
def checkBagExistByID(request, bagid):
    if request.method == 'GET':
        result = "true" if db.check_if_bag_exists(bagid) else "false"
        return HttpResponse(result)


@ api_view(['GET', 'PUT', 'DELETE'])
def removeAllDataByID(request, bagid):
    logger.info("into delete ")
    print(request.method)
    if request.method == 'DELETE' or request.method == 'GET':
        logger.info(" into request delete")
        result = "done" if db.remove_all_data_by_id(bagid) else "failed"
        logger.info("return ")
        return HttpResponse(result)


@ api_view(['GET', 'PUT', 'DELETE'])
def getAllTimestampsByID(request, bagid):
    if request.method == 'GET':
        logger.info("into get association")
        return HttpResponse(db.get_all_timestamps_by_id(bagid))


@ api_view(['GET', 'PUT', 'DELETE'])
def getFrameByIdTime(request, bagid, timestamp):
    if request.method == 'GET':
        return HttpResponse(db.get_frame_by_id_time(bagid, timestamp))

# This will be directly used by C++ SYNC mode, so only return value


@ api_view(['POST'])
def uploadSceneResultOne(request):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_scene_result_one(data_dict)
        return HttpResponse("done")


@ api_view(['GET', 'PUT', 'DELETE'])
def getMessageByIdTimeTopicVersion(request, bagid, timestamp, topic, version):
    if request.method == 'GET':
        message = db.get_message_by_id_time_topic_version(
            bagid, timestamp, topic, version)
        return HttpResponse(message)


@ api_view(['GET', 'POST', 'DELETE'])
def uploadMessageByIdTimeTopicVersion(request, bagid, timestamp, topic, version):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_message_by_id_time_topic_version(
                data_dict, bagid, timestamp, topic, version)
        return HttpResponse("done")


@ api_view(['GET', 'PUT', 'DELETE'])
def getRangeMessageByIdTopic(request, bagid, topic, start, end):
    if request.method == 'GET':
        return HttpResponse(db.get_range_message_by_id_topic(bagid, topic, start, end))


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
def uploadTrajectoryInfoById(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        print("into put")
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_trajectoryinfo_by_id(request_dict.get("data"), request_dict.get("bagid")))


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadTrajectoryAttri(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_attri_by_id(request_dict.get("data"), request_dict.get("bagid")))


# labeling related


@ api_view(['GET', 'PUT', 'DELETE'])
def uploadLabelingIndexById(request):
    print("before into %s" % request.method)
    if request.method == 'PUT' and request is not None:
        request_body = request.data
        request_dict = request_body.dict()
        return JsonResponse(db.upload_labeling_index_by_id(request_dict.get("data"), request_dict.get("bagid")))


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
        return JsonResponse(db.upload_labeling_time_by_id(request_dict.get("data"), request_dict.get("bagid")))


@ api_view(['GET', 'PUT', 'DELETE'])
def getLabelingTimeById(request, bagid, index):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_labeling_time_by_id(bagid, index)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getLabelingData(request, bagid, anotation_type, frame_index):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_labeling_data(bagid, anotation_type, frame_index)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getLabelingDataByPost(request):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            return JsonResponse({'result': db.get_labeling_data_by_post(data_dict)})


@ api_view(['GET', 'PUT', 'DELETE'])
def getMultiLabelingInfoById(request, bagid, start, end):
    if request.method == 'GET':
        return JsonResponse({'result': db.get_multi_labelinginfo_by_id(bagid, start, end)})

# task related


@ api_view(['GET', 'POST', 'DELETE'])
def uploadTaskInfo(request, taskid, play_mode, scene_id, subscene_id, planning_version, perception_version):
    if request.method == 'POST':
        db.upload_task_info(
            taskid, play_mode, scene_id, subscene_id, planning_version, perception_version)
        return HttpResponse("done")


@ api_view(['GET', 'PUT', 'DELETE'])
def getTaskInfoById(request, taskid):
    if request.method == 'GET':
        return JsonResponse(db.get_taskinfo_by_id(taskid))


# task/frame result related

@ api_view(['POST'])
def uploadTaskResultByIDVersionMode(request, taskid, grading_version, play_mode):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_task_result_by_id_version_mode(
                data_dict, taskid, grading_version, play_mode)
        return HttpResponse("done")


@ api_view(['POST'])
def uploadTaskFrameResultByIDVersionTime(request, taskid, grading_version, timestamp):
    if request.method == 'POST':
        if request.data is not None:
            data_dict = request.data.dict()
            db.upload_task_frame_result_by_id_version_time(
                data_dict, taskid, grading_version, timestamp)
        return HttpResponse("done")


@ api_view(['GET'])
def getTaskResultByIDVersionMode(request, taskid, grading_version, play_mode):
    if request.method == 'GET':
        result_str = db.get_task_result_by_id_version_mode(
            taskid, grading_version, play_mode)
        return JsonResponse({'result': result_str})


@ api_view(['GET'])
def getTaskFrameResultByIDVersionMode(request, taskid, grading_version, timestamp):
    if request.method == 'GET':
        result_str = db.get_task_frame_result_by_id_version_time(
            taskid, grading_version, timestamp)
        return JsonResponse({'debug_info': result_str})


# result related

@ api_view(['GET'])
def getSceneResultAggregation(request):
    if request.method == 'GET':
        if request.data is not None:
            filters = eval(request.GET.get("filters", ""))
            sets = eval(request.GET.get("sets", ""))
            aggregation_methods = eval(
                request.GET.get("aggregation_methods", ""))
            list_of_json_res = db.get_scene_result_aggregation(
                filters, sets, aggregation_methods)
            return JsonResponse({"res": str(list_of_json_res)})


@ api_view(['GET'])
def getGradingResultAggregation(request):
    if request.method == 'GET':
        if request.data is not None:
            filters = eval(request.GET.get("filters", ""))
            aggregation_methods = eval(
                request.GET.get("aggregation_methods", ""))
            projects = eval(
                request.GET.get("projects", ""))
            one_json_res = db.get_grading_result_aggregation(
                filters, aggregation_methods, projects)
            return JsonResponse({"res": str(one_json_res)})
