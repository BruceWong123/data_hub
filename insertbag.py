from pymongo import MongoClient
import urllib.parse
import time
import random
import redis

import mysql.connector as mysql

# enter your server IP address/domain name
HOST = "34.218.26.149"  # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = ""
# this is the user you create
USER = "deeproute"
# user password
PASSWORD = "deeproute"
# connect to MySQL server
db_connection = mysql.connect(
    host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", db_connection.get_server_info())
# enter your code here!


username = urllib.parse.quote_plus('deep')
password = urllib.parse.quote_plus('route')

myclient = MongoClient(
    'mongodb://%s:%s@34.218.26.149/datahub' % (username, password))
mydb = myclient["datahub"]
collist = mydb.list_collection_names()
if "messages" in collist:
    print("The collection exists.")

mycol = mydb["messages"]
timestamp_test = 1583635929485759997
testitem = {"topic": "/test2", "timestamp": timestamp_test}
mycol.insert_one(testitem)
result = mycol.find({"topic": {"$regex": "^/t"}})

for x in result:
    print("result: ", x.get('topic'), " timestamp: ",
          x.get('timestamp'), " id: ", x.get('_id'))
