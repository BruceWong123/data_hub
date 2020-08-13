from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Bag
from .serializers import *

from pymongo import MongoClient
import urllib.parse
import time

username = urllib.parse.quote_plus('deep')
password = urllib.parse.quote_plus('route')

myclient = MongoClient(
    'mongodb://%s:%s@34.218.26.149/datahub' % (username, password))
mydb = myclient["datahub"]
collist = mydb.list_collection_names()
if "messages" in collist:
    print("The collection exists.")


@login_required(login_url="/login/")
def index(request):
    return render(request, "index2.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def uploadFile(request):
    if 'inputDescription' in request.POST:
        mapname = request.POST['inputDescription']
        if not mapname:
            return HttpResponse("missing value for map name")
        else:
            return HttpResponse("%s" % mapname)
    else:
        return HttpResponse("missing map name")


@api_view(['GET', 'POST'])
def getAllBags(request):
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        bags = Bag.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(bags, 5)
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
def getBagByIDAndTimestamp(request, bagid, time):
    context = {}
    try:
        bag = Bag.objects.get(bagid=bagid)
        stime = int(time)
        start = int(bag.start)
        end = int(bag.end)
        if stime < start or stime > end:
            return HttpResponse("time stamp is out of range with range start from %s " % stime)
    except Bag.DoesNotExist:
        return HttpResponse("can't find by id: %s" % pk)

    if request.method == 'GET':
        serializer = BagSerializer(bag, context={'request': request})

        # return Response(serializer.data)

        mycol = mydb["messages"]
        #result = mycol.find({"topic": {"$regex": "^/p"}}).limit(1)
        result = mycol.find({"timestamp": {"$lte": time}}).limit(3)
        resultstr = result.count()
        for x in result:
            resultstr = x["topic"] + ":" + x["message"]

        return HttpResponse("return data for bag with timestamp %s" % resultstr)

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
def getBagByID(request, bagid):
    context = {}
    try:
        bag = Bag.objects.get(bagid=bagid)
    except Bag.DoesNotExist:
        # html_template = loader.get_template('page-404.html')
        return HttpResponse("can't find by id: %s" % bagid)

    if request.method == 'GET':
        serializer = BagSerializer(bag, context={'request': request})
        return HttpResponse("return data for bag:  %s" % serializer.data)
        # return Response(serializer.data)

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
def getBagByCity(request, city):
    context = {}
    try:
        bag = Bag.objects.get(city=city)
    except Bag.DoesNotExist:
        # html_template = loader.get_template('page-404.html')
        return HttpResponse("can't find city by %s" % city)

    if request.method == 'GET':
        serializer = BagSerializer(bag, context={'request': request})
        return HttpResponse("return data for bag:  %s" % serializer.data)
        # return Response(serializer.data)

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
