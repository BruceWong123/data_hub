from test_trajectory_upload import Test_trajectory_upload
from test_trajectory_download import Test_trajectory_download
from test_labeling_upload import Test_labeling_upload
from test_labeling_download import Test_labeling_download


if __name__ == '__main__':
    test = Test_trajectory_upload()
    # test.upload_attributes()
    test.test_upload_trajectory_by_dict()
    # test.test_download_labeling_data()
    # test.test_mongo()
    print("try to get")
