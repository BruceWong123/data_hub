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
    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.getAllTimestampsByID),

    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<time>[0-9]+)/$',
        views.api.getFrameByIdTime),

    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<topic>[0-9a-zA-Z_]+)/$',
        views.api.getAllTopicsByID),

    url(r'^api/bags/(?P<bagid>[0-9a-zA-Z_]+)/(?P<time>[0-9]+)/(?P<topic>[0-9a-zA-Z_]+)/$',
        views.api.getMessageByIdTimeTopic),

    url(r'^api/citys/(?P<city>[a-zA-Z]+)/$', views.api.getBagByCity),


    url(r'^(?!/api).*$', views.views.pages, name='pages'),
]
