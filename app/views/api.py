from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Bag
from ..serializers import *

from pymongo import MongoClient
import urllib.parse
import time
import base64
import mysql.connector as mysql

import json
import logging
logger = logging.getLogger(__name__)

username = urllib.parse.quote_plus('deep')
password = urllib.parse.quote_plus('route')

mongo_client = MongoClient(
    'mongodb://%s:%s@10.9.9.9:%s/datahub' % (username, password, "30002"))
mongo_db = mongo_client["datahub"]
db_messages = mongo_db["messages"]
db_frame_results = mongo_db["frame_results"]
db_bag_results = mongo_db["bag_results"]
HOST = "34.218.26.149"
DATABASE = "data_hub"
USER = "root"
PASSWORD = "123456"
PORT = "12345"
mysql_db = mysql.connect(host=HOST, database=DATABASE,
                         user=USER, password=PASSWORD, port=PORT)


@api_view(['GET', 'POST'])
def getAllBags(request):
    if request.method == 'GET':
        data = []
        bags = Bag.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(bags, 100)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        serializer = BagSerializer(
            data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()
        return HttpResponse("return data for bags:  %s" % serializer.data)
    elif request.method == 'POST':
        serializer = BagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getAllTopicsByID(request, bagid, topic):
    try:
        bag = Bag.objects.get(bagid=bagid)
    except Bag.DoesNotExist:
        return HttpResponse("can't find by id: %s" % bagid)
    if request.method == 'GET':
        result = ""
        if topic == 'topics':
            mysql_db = mysql.connect(host=HOST, database=DATABASE,
                                     user=USER, password=PASSWORD, port=PORT)
            mycursor = mysql_db.cursor()
            sql = "SELECT name FROM app_topic WHERE bagid = %s"
            adr = (bagid, )
            mycursor.execute(sql, adr)
            myresult = mycursor.fetchall()
            for row in myresult:
                result += " "
                result += str(row[0])
            mycursor.close()
            mysql_db.close()
        return HttpResponse("%s" % result)
    elif request.method == 'PUT':
        serializer = BagSerializer(
            bag, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        bag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@ api_view(['GET', 'PUT', 'DELETE'])
def getAllTimestampsByID(request, bagid):
    if request.method == 'GET':
        mysql_db = mysql.connect(host=HOST, database=DATABASE,
                                 user=USER, password=PASSWORD, port=PORT)
        mycursor = mysql_db.cursor()
        sql = "SELECT association FROM app_association WHERE bagid = %s"
        adr = (bagid, )
        mycursor.execute(sql, adr)
        myresult = mycursor.fetchall()
        result = ""
        for row in myresult:
            result += " "
            result += str(row[0])
        logger.warning("Your log message is here")
        mycursor.close()
        mysql_db.close()
        return HttpResponse("%s" % result)


@ api_view(['GET', 'PUT', 'DELETE'])
def getFrameByIdTime(request, bagid, time):
    if request.method == 'GET':
        result = db_messages.find({"bagid": bagid, "timestamp": {"$lte": time}, "topic": {
            "$regex": "^/perception/objects"}})
        resultstr = "no data found"
        for x in result:
            y = db_messages.find_one({"$and": [{"bagid": bagid, "topic": {
                "$regex": "^/canbus/car_state"}}, {"timestamp": {"$lte": time}}]}, sort=[("timestamp", -1)])
            if not y:
                break
            resultstr = y.get('message') + " | " + x["message"]

        return HttpResponse("%s" % resultstr)


def translateTopic(topic):
    if topic == 'perception':
        return '/perception/objects'
    elif topic == 'carstate':
        return '/canbus/car_state'
    elif topic == 'signals_response':
        return '/perception/signals_response'
    elif topic == 'context':
        return '/planner/context'
    elif topic == 'debug_info':
        return '/planner/debug_info'


@ api_view(['GET', 'PUT', 'DELETE'])
def getMessageByIdTimeTopic(request, bagid, time, topic):
    if request.method == 'GET':
        topic = translateTopic(topic)
        result = db_messages.find(
            {"bagid": bagid, "timestamp": time, "topic": topic})
        resultstr = " "
        for x in result:
            resultstr = x['message']
        return HttpResponse(resultstr)


@ api_view(['GET', 'PUT', 'DELETE'])
def getMessageByIdTimeTopicRange(request, bagid, topic, start, end):
    if request.method == 'GET':
        topic = translateTopic(topic)
        result = db_messages.find(
            {"bagid": bagid, "timestamp": {'$lte': end, '$gte': start}, "topic": topic})
        resultstr = ""
        for i, x in enumerate(result):
            resultstr += x['message']
            if i != result.count() - 1:
                resultstr += "deep_route"
        return HttpResponse(resultstr)


@ api_view(['GET', 'PUT', 'DELETE'])
def getBagByCity(request, city):
    try:
        bag = Bag.objects.filter(city=city)
        return HttpResponse("found city by %s" % city)
    except Bag.DoesNotExist:
        return HttpResponse("can't find city by %s" % city)
    if request.method == 'GET':
        return HttpResponse("can't find city by %s" % city)
    elif request.method == 'PUT':
        serializer = BagSerializer(
            bag, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@ api_view(['POST'])
def uploadBagResultByIDVersionMode(request, bagid, function_version, grading_version, play_mode):
    if request.method == 'POST':
        if request.data is None:
            return
        data = db_bag_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "play_mode": play_mode})
        if data is None:
            if request.data is not None:
                data_dict = {
                    "bagid": bagid,
                    "function_version": function_version,
                    "grading_version": grading_version,
                    "play_mode": play_mode,
                    "result": request.data
                }
                db_bag_results.insert_one(data_dict)
        else:
            db_bag_results.update(
                {
                    "_id": data.get('_id')
                },
                {"$set": {
                    "result": request.data
                }
                }
            )


@ api_view(['GET'])
def getBagResultByIDVersionMode(request, bagid, function_version, grading_version, play_mode):
    if request.method == 'GET':
        if request.data is None:
            return
        data = db_bag_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "play_mode": play_mode})
        if data is None:
            return ""
        else:
            return data.get('result')


@ api_view(['POST'])
def uploadFrameResultByIDVersionTime(request, bagid, function_version, grading_version, timestamp):
    if request.method == 'POST':
        if request.data is None:
            return
        key = list(request.data.keys())[0]
        value = list(request.data.values())[0]
        data = db_frame_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "timestamp": timestamp})
        if data is None:
            if request.data is not None:
                data_dict = {
                    "bagid": bagid,
                    "function_version": function_version,
                    "grading_version": grading_version,
                    "timestamp": timestamp,
                    key: value
                }
                db_frame_results.insert_one(data_dict)
        else:
            db_frame_results.update(
                {
                    "_id": data.get('_id')
                },
                {"$set": {
                    key: value
                }
                }
            )


@ api_view(['GET'])
def getFrameResultByIDVersionTime(request, bagid, function_version, grading_version, timestamp):
    if request.method == 'GET':
        if request.data is None:
            return
        data = db_frame_results.find_one(
            {"bagid": bagid, "function_version": function_version, "grading_version": grading_version, "timestamp": timestamp})
        if data is None:
            return {}
        else:
            result = data.get('debug_info')
            return {"debug_info": list(result.values())[0]}
