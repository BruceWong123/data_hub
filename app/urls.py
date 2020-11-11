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

    url(r'^api/bags/$', views.api.getAllBags),

    # upload column into result
    url(r'^api/upload/(?P<bagid>[0-9a-zA-Z_]+)/(?P<version>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/$',
        views.api.uploadNewDataByIDVersionTime),

    # get all matching timestamps by bagid
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.getAllTimestampsByID),

    # get data for whole frame given bag id and timestamp
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<time>[0-9]+)/$',
        views.api.getFrameByIdTime),

    # # get all topics names by bag id
    # url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<topic>[0-9a-zA-Z_]+)/$',
    #     views.api.getAllTopicsByID),

    # get body of message for certain topic given bag id and timestamp
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<time>[0-9]+)/(?P<topic>[0-9a-zA-Z_]+)/$',
        views.api.getMessageByIdTimeTopic),

    # get body of message for certain topic given bag id and timestamp
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<topic>[0-9a-zA-Z_]+)/(?P<start>[0-9]+)/(?P<end>[0-9]+)/$',
        views.api.getMessageByIdTimeTopicRange),


    url(r'^api/citys/(?P<city>[a-zA-Z]+)/$', views.api.getBagByCity),


    url(r'^(?!/api).*$', views.views.pages, name='pages'),
]
