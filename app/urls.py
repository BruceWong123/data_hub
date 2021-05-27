# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from app import views
from django.conf.urls import url

urlpatterns = [

    path('', views.views.index, name='home'),
    url('uploadFile', views.views.uploadFile),

    # upload row into scene result
    url(r'^api/upload/scene_result_one/$', views.api.uploadSceneResultOne),

    # upload column into frame result
    url(r'^api/upload/(?P<taskid>[0-9a-zA-Z_]+)/(?P<grading_version>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/$',
        views.api.uploadTaskFrameResultByIDVersionTime),

    # upload column into bag result
    url(r'^api/upload/(?P<taskid>[0-9a-zA-Z_]+)/(?P<grading_version>[0-9a-zA-Z_]+)/(?P<play_mode>[a-zA-Z_]+)/$',
        views.api.uploadTaskResultByIDVersionMode),

    # upload row into scene result
    url(r'^api/upload/scene_result_one/$',
        views.api.uploadSceneResultOne),

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



    # Trajectory related
    # test get trajectory
    url(r'^api/trajectory/download/(?P<bagid>[0-9a-zA-Z_]+)/$',
        views.api.getTrajectoryInfoById),

    # upload trajectory
    url(r'^api/trajectory/upload/$',
        views.api.uploadTrajectoryInfoById),


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


    # download single frame trajectory
    url(r'^api/trajectory/data/(?P<bagid>[0-9a-zA-Z_]+)/(?P<timestamp>[0-9]+)/(?P<objectid>[0-9]+)/(?P<seqlen>[0-9]+)/$',
        views.api.getTrajectoryData),

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
    url(r'^api/labeling/data/download/$',
        views.api.getLabelingDataByPost),

    # download labeling data multiple frame
    url(r'^api/labeling/(?P<bagid>[0-9a-zA-Z_]+)/(?P<start>[0-9]+)/(?P<end>[0-9]+)/$',
        views.api.getMultiLabelingInfoById),

    url(r'^(?!/api).*$', views.views.pages, name='pages'),

]
