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

username = urllib.parse.quote_plus('deep')
password = urllib.parse.quote_plus('route')

mongo_client = MongoClient(
    'mongodb://%s:%s@34.218.26.149/datahub' % (username, password))
mongo_db = mongo_client["datahub"]
mongo_col = mongo_db["messages"]


@api_view(['GET', 'POST'])
def getAllBags(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
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
        # return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages, 'nextlink': '/api/bags/?page=' + str(nextPage), 'prevlink': '/api/bags/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = BagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getAllTopicsByID(request, bagid):
    context = {}
    try:
        bag = Bag.objects.get(bagid=bagid)
    except Bag.DoesNotExist:
        # html_template = loader.get_template('page-404.html')
        return HttpResponse("can't find by id: %s" % bagid)

    if request.method == 'GET':

        result = mongo_col.find(
            {"bagid": bagid, "topic": {"$regex": "^/perception/objects"}}, sort=[("timestamp", 1)]).limit(1000)
        resultstr = ""
        for x in result:
            resultstr += "{" + x["timestamp"] + "}"

        return HttpResponse("all timestamps :  %s" % resultstr)
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


@api_view(['GET', 'PUT', 'DELETE'])
def getBagByID(request, bagid):
    context = {}
    try:
        bag = Bag.objects.get(bagid=bagid)
    except Bag.DoesNotExist:
        # html_template = loader.get_template('page-404.html')
        return HttpResponse("can't find by id: %s" % bagid)

    if request.method == 'GET':
        # serializer = BagSerializer(bag, context={'request': request})
        # return HttpResponse("return data for bag:  %s" % serializer.data)
        # return Response(serializer.data)

        result = mongo_col.find(
            {"bagid": bagid, "topic": {"$regex": "^/perception/objects"}}, sort=[("timestamp", 1)]).limit(1000)
        resultstr = ""
        for x in result:
            resultstr += "{" + x["timestamp"] + "}"

        return HttpResponse("all timestamps :  %s" % resultstr)
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


@api_view(['GET', 'PUT', 'DELETE'])
def getBagByIdTime(request, bagid, time):
    try:
        bag = Bag.objects.get(bagid=bagid)
        stime = int(time)
        start = int(bag.start)
        end = int(bag.end)
        if stime < start or stime > end:
            return HttpResponse("time stamp is out of range with range start from %s " % end)
    except Bag.DoesNotExist:
        return HttpResponse("can't find by id: %s" % bagid)

    if request.method == 'GET':
        serializer = BagSerializer(bag, context={'request': request})
        result = mongo_col.find(
            {"timestamp": {"$lte": time}, "topic": {"$regex": "^/perception/objects"}})
        resultstr = "no data found"
        for x in result:
            y = mongo_col.find_one({"$and": [{"topic": {
                "$regex": "^/canbus/car_state"}}, {"timestamp": {"$lte": time}}]}, sort=[("timestamp", -1)])
            if not y:
                break
            resultstr = y.get('message') + " | " + x["message"]

        return HttpResponse("%s" % resultstr)

    elif request.method == 'PUT':
        serializer = BagSerializer(
            bag, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse("put in get bag by id and time stamp")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bag.delete()
        return HttpResponse("delete in get bag by id and time stamp")
        # return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def getBagByIdTimeTopic(request, bagid, time, topic):
    try:
        bag = Bag.objects.get(bagid=bagid)
        stime = int(time)
        start = int(bag.start)
        end = int(bag.end)
        if stime < start or stime > end:
            return HttpResponse("time stamp is out of range : %s " % stime)
    except Bag.DoesNotExist:
        return HttpResponse("can't find by id: %s" % bagid)

    if request.method == 'GET':
        if topic == 'perception':
            topic = '/perception/objects'
        elif topic == 'carstate':
            topic = '/canbus/car_state'
        result = mongo_col.find(
            {"timestamp": {"$lte": time}, "topic": topic})
        resultstr = result.count()
        for x in result:
            resultstr = x['message']
        binarystr = base64.b64decode(resultstr)
        return HttpResponse(binarystr)

    elif request.method == 'PUT':
        serializer = BagSerializer(
            bag, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse("put in get bag by id and time stamp")
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bag.delete()
        return HttpResponse("delete in get bag by id and time stamp")
        # return Response(status=status.HTTP_204_NO_CONTENT)


@ api_view(['GET', 'PUT', 'DELETE'])
def getBagByCity(request, city):
    try:
        bag = Bag.objects.filter(city=city)
        return HttpResponse("found city by %s" % city)
    except Bag.DoesNotExist:
        # html_template = loader.get_template('page-404.html')
        return HttpResponse("can't find city by %s" % city)

    if request.method == 'GET':
        # serializer = BagSerializer(bag, context={'request': request})
        # return HttpResponse("return data for bag:  %s" % serializer.data)
        # return Response(serializer.data)
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
