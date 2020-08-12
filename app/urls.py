# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from django.conf.urls import url

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    url('uploadFile', views.uploadFile),
    #path('test', views.uploadFile),
    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),


    url(r'^api/bags/$', views.getAllBags),
    url(r'^api/bags/(?P<pk>[0-9]+)$', views.getBagByID),

    url(r'^api/bags/(?P<pk>[0-9]+)/(?P<time>[0-9]+)/$',
        views.getBagByIDAndTimestamp),
    url(r'^api/bags/(?P<city>[a-zA-Z]+)$', views.getBagByCity),
]
