from test_trajectory_upload import Test_trajectory_upload
from test_trajectory_download import Test_trajectory_download
from test_labeling_upload import Test_labeling_upload
from test_labeling_download import Test_labeling_download
import configparser
import os
import time


def test_traj_upload():

    test_upload = Test_trajectory_upload()

    start_time = round(time.time() * 1000)
    test_upload.test_upload_trajectory_by_file(1)
    end_time = round(time.time() * 1000)
    print("upload 1 trajectory within %d ms " % (end_time-start_time))

    start_time = round(time.time() * 1000)
    test_upload.test_upload_trajectory_by_file(100)
    end_time = round(time.time() * 1000)
    print("upload 100 trajectory within %d ms " % (end_time-start_time))

    start_time = round(time.time() * 1000)
    test_upload.test_upload_trajectory_by_file(1000)
    end_time = round(time.time() * 1000)
    print("upload 1000 trajectory within %d ms " % (end_time-start_time))

    # start_time = round(time.time() * 1000)
    # test_upload.test_upload_attributes_by_file(1)
    # end_time = round(time.time() * 1000)
    # print("upload 1 frames attributes within %d ms " % (end_time-start_time))

    # start_time = round(time.time() * 1000)
    # test_upload.test_upload_attributes_by_file(10)
    # end_time = round(time.time() * 1000)
    # print("upload 10 frames attributes within %d ms " % (end_time-start_time))

    # start_time = round(time.time() * 1000)
    # test_upload.test_upload_attributes_by_file(100)
    # end_time = round(time.time() * 1000)
    # print("upload 100 frames attributes within %d ms " % (end_time-start_time))


def test_traj_download():
    test_download = Test_trajectory_download()
    start_time = round(time.time() * 1000)
    is_still_10_traj = test_download.test_download_trajectory_data(
        "is_still", 10)
    is_still_10_compare = result_config.get("TRAJ", "is_still_10")
    if is_still_10_traj != is_still_10_compare:
        print("Fail is_still_10")
    else:
        end_time = round(time.time() * 1000)
        print("is_still_10 passed within %d ms " % (end_time-start_time))

    start_time = round(time.time() * 1000)
    is_still_20_traj = test_download.test_download_trajectory_data(
        "is_still", 20)
    is_still_20_compare = result_config.get("TRAJ", "is_still_20")
    if is_still_20_traj != is_still_20_compare:
        print("Fail is_still 20")
    else:
        end_time = round(time.time() * 1000)
        print("is_still_20 passed within %d ms " % (end_time-start_time))

    start_time = round(time.time() * 1000)
    query_dict = dict()
    query_dict["is_still"] = "true"
    query_dict["on_lane"] = "false"
    is_still_on_lane_traj = test_download.test_download_trajectory_data_multiattributes(
        query_dict)
    is_still_on_lane_compare = result_config.get("TRAJ", "is_still_on_lane_50")
    if is_still_on_lane_traj != is_still_on_lane_compare:
        print("Fail is_still_on_lane_50")
    else:
        end_time = round(time.time() * 1000)
        print("is_still_10 passed within %d ms" % (end_time-start_time))


def test_labeling_upload():
    test_upload = Test_labeling_upload()

    start_time = round(time.time() * 1000)
    test_upload.test_upload_labeling()
    end_time = round(time.time() * 1000)
    print("upload labeling index data passed within %d ms" %
          (end_time-start_time))

    start_time = round(time.time() * 1000)
    test_upload.test_upload_labeling_data()
    end_time = round(time.time() * 1000)
    print("upload labeling data passed within %d ms" % (end_time-start_time))

    start_time = round(time.time() * 1000)
    test_upload.test_upload_labeling_data2()
    end_time = round(time.time() * 1000)
    print("upload labeling init data passed within %d ms" %
          (end_time-start_time))


def test_labeling_download():
    test_download = Test_labeling_download()
    labeling_download_compare = result_config.get("LABELING", "download")

    start_time = round(time.time() * 1000)
    result = test_download.test_downloading_labeling_data()
    end_time = round(time.time() * 1000)

    if labeling_download_compare != result:
        print("Fail downloading labeling")
    else:
        print("download labeling data passed within %d ms" %
              (end_time-start_time))


if __name__ == '__main__':
    result_config = configparser.ConfigParser()
    result_config.read(os.path.abspath(
        os.path.dirname(__file__)) + "/test_result.ini")

    test_traj_upload()

    test_traj_download()

    test_labeling_upload()

    test_labeling_download()

    print("All test passed!")
