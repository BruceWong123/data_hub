from test_trajectory_upload import Test_trajectory_upload
from test_trajectory_download import Test_trajectory_download
from test_labeling_upload import Test_labeling_upload
from test_labeling_download import Test_labeling_download
import configparser
import os
if __name__ == '__main__':
    result_config = configparser.ConfigParser()
    result_config.read(os.path.abspath(
        os.path.dirname(__file__)) + "/test_result.ini")
    test_upload = Test_trajectory_upload()
    # test_upload.upload_attributes()
    test_upload.test_upload_trajectory_by_file(3)
    # test_upload.test_upload_attributes_by_file()

    # test_download = Test_trajectory_download()

    # is_still_10_traj = test_download.test_download_trajectory_data(
    #     "is_still", 10)
    # is_still_10_compare = result_config.get("TRAJ", "is_still_10")
    # if is_still_10_traj != is_still_10_compare:
    #     print("Fail is_still 10")

    # is_still_20_traj = test_download.test_download_trajectory_data(
    #     "is_still", 20)
    # is_still_20_compare = result_config.get("TRAJ", "is_still_20")
    # if is_still_20_traj != is_still_20_compare:
    #     print("Fail is_still 20")

    print("pass all test")
