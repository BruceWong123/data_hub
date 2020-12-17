# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url

urlpatterns = [

    path('', views.views.index, name='home'),
    url('uploadFile', views.views.uploadFile),


    # upload column into frame result
    url(r'^api/upload/(?P<taskid>[0-9a-zA-Z_]+)/(?P<grading_version>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/$',
        views.api.uploadTaskFrameResultByIDVersionTime),

    # upload column into bag result
    url(r'^api/upload/(?P<taskid>[0-9a-zA-Z_]+)/(?P<grading_version>[0-9a-zA-Z_]+)/(?P<play_mode>[a-zA-Z_]+)/$',
        views.api.uploadTaskResultByIDVersionMode),



    # get data from scene result
    url(r'^api/results/scene_result_aggregation/$',
        views.api.getSceneResultAggregation),

    # get data from grading result
    url(r'^api/results/grading_result_aggregation/$',
        views.api.getGradingResultAggregation),

    # get data from frame result
    url(r'^api/results/(?P<taskid>[0-9a-zA-Z_]+)/(?P<grading_version>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/$',
        views.api.getTaskFrameResultByIDVersionMode),

    # get data from bag result
    url(r'^api/results/(?P<taskid>[0-9a-zA-Z_]+)/(?P<grading_version>[0-9a-zA-Z_]+)/(?P<play_mode>[a-zA-Z_]+)/$',
        views.api.getTaskResultByIDVersionMode),

    # get all bagid
    url(r'^api/bags/all/$',
        views.api.getAllBagID),

    # check if bag exist
    url(r'^api/exist/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.checkBagExistByID),

    # remove all data by bagid
    url(r'^api/delete/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.removeAllDataByID),

    # get all matching timestamps by bagid
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.getAllTimestampsByID),

    # get data for whole frame given bag id and timestamp
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/$',
        views.api.getFrameByIdTime),

    # upload message for certain topic with specific version by bag id and timestamp
    url(r'^api/bags/upload/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/(?P<topic>[0-9a-zA-Z_]+)/(?P<version>[0-9a-zA-Z_]+)/$',
        views.api.uploadMessageByIdTimeTopicVersion),

    # get body of message for certain topic given bag id and timestamp
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/(?P<topic>[0-9a-zA-Z_]+)/(?P<version>[0-9a-zA-Z_]+)/$',
        views.api.getMessageByIdTimeTopicVersion),

    # get body of message for certain topic given bag id and timestamp
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<topic>[0-9a-zA-Z_]+)/(?P<start>[0-9]+)/(?P<end>[0-9]+)/$',
        views.api.getRangeMessageByIdTopic),


    # upload taskinfo
    url(r'^api/tasks/upload/(?P<taskid>[0-9a-zA-Z_]+)/(?P<play_mode>[0-9a-zA-Z_]+)/(?P<scene_id>[0-9a-zA-Z_]+)/(?P<subscene_id>[0-9a-zA-Z_]+)/(?P<planning_version>[0-9a-zA-Z_]+)/(?P<perception_version>[0-9a-zA-Z_]+)/$',
        views.api.uploadTaskInfo),

    # get data for taskinfo
    url(r'^api/tasks/(?P<taskid>[0-9a-zA-Z_]+)/$',
        views.api.getTaskInfoById),

    url(r'^(?!/api).*$', views.views.pages, name='pages'),
]
