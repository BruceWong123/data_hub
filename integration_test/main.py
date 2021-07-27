from uploading_test import Uploading_test
from downloading_test import Downloading_test


if __name__ == '__main__':
    test = Uploading_test()
    # test.upload_attributes()
    test.upload_trajectory_by_dict()
    # test.download_labeling_data()
    # test.test_mongo()
    print("try to get")
    # body = requests.get("http://www.baidu.com")
    # print(body)
