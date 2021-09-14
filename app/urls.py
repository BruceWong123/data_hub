# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views
from django.conf.urls import url

urlpatterns = [

    path('', views.views.index, name='home'),
    url('uploadFile', views.views.uploadFile),

    # Trajectory related
    # test get trajectory
    url(r'^api/trajectory/download/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.getTrajectoryInfoById),

    # upload trajectory
    # url(r'^api/trajectory/upload/$',
    #     views.api.uploadTrajectoryInfoById),


    url(r'^api/consistency_test/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.consistencyCheck),

    # upload trajectory
    url(r'^api/trajectory/upload/$',
        views.api.uploadTrajectoryInfoByDict),

    # upload object info
    url(r'^api/object_info/upload/$',
        views.api.uploadObjectInfoByDict),

    # upload bag info
    url(r'^api/bag_info/upload/$',
        views.api.uploadBagInfoByDict),

    # evaluate trajectory
    url(r'^api/trajectory/evaluate/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.evaluateTrajectoryById),

    # get all bagids
    url(r'^api/trajectory/bags/all/$',
        views.api.getBagidsInTrajectory),

    # given bagid, get all timestamps in that bag
    url(r'^api/trajectory/timestamps/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.getTimestampsByBagid),

    # given timestamp, get all objectid has trajectory
    url(r'^api/trajectory/objects/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/$',
        views.api.getObjectsByTimestamp),

    # given timestamp, get all trajectory attribute
    url(r'^api/trajectory/attributes/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/$',
        views.api.getTrajectoryAttri),

    # given bagid, timestamp, upload attribute
    url(r'^api/trajectory/attributes/upload/$',
        views.api.uploadTrajectoryAttri),

    # given timestamp, attribute, get all objectid has trajectory in that attribute
    url(r'^api/trajectory/objects/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/(?P<feature>[a-zA-Z_]+)/$',
        views.api.getObjectsByFeature),


    # download single frame trajectory by attribute
    url(r'^api/trajectory/data/multiattributes/download/',
        views.api.getTrajectoryDataByMultiAttribute),

    # download single frame trajectory
    url(r'^api/trajectory/data/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/(?P<objectid>[0-9]+)/(?P<seqlen>[0-9]+)/$',
        views.api.getTrajectoryData),

    # download single frame trajectory by attribute
    url(r'^api/trajectory/data/(?P<attribute>[a-zA-Z_]+)/(?P<seqlen>[0-9]+)/$',
        views.api.getTrajectoryDataByAttribute),

    # download single frame trajectory by attribute
    url(r'^api/trajectory/data/(?P<attribute>[a-zA-Z_]+)/(?P<seqlen>[0-9]+)/(?P<seqnum>[0-9]+)/$',
        views.api.getMultipleTrajectoryDataByAttribute),

    # download multiple frame trajectory
    url(r'^api/trajectory/data/(?P<bagid>[0-9a-zA-Z_]+)/(?P<start_time>[0-9]+)/(?P<end_time>[0-9]+)/(?P<objectid>[0-9]+)/(?P<seqlen>[0-9]+)/$',
        views.api.getMultiTrajectoryData),



    # label related

    # upload labeling
    url(r'^api/labeling/time/upload/$',
        views.api.uploadLabelingTimeById),

    # download labeling data
    url(r'^api/labeling/time/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.getLabelingTimeById),

    # upload labeling
    url(r'^api/labeling/index/upload/$',
        views.api.uploadLabelingIndexById),

    # download labeling data
    url(r'^api/labeling/index/(?P<bagid>[0-9a-zA-Z_]+)/(?P<topic>[0-9a-zA-Z_]+)/$',
        views.api.getLabelingIndexById),

    # download labeling data multiple frame
    url(r'^api/labeling/(?P<bagid>[0-9a-zA-Z_]+)/(?P<anotation_type>[0-9a-zA-Z_]+)/(?P<frame_index>[0-9]+)/$',
        views.api.getLabelingData),

    # download labeling data multiple frame
    url(r'^api/labeling/data/upload/$',
        views.api.uploadLabelingData),

    # download labeling data multiple frame
    url(r'^api/labeling/data/first_upload/$',
        views.api.uploadLabelingDataInit),

    # download labeling data multiple frame
    url(r'^api/labeling/data/download/$',
        views.api.getLabelingDataByPost),

    # download labeling data multiple frame
    url(r'^api/labeling/(?P<bagid>[0-9a-zA-Z_]+)/(?P<start>[0-9]+)/(?P<end>[0-9]+)/$',
        views.api.getMultiLabelingInfoById),

    url(r'^(?!/api).*$', views.views.pages, name='pages'),

]
