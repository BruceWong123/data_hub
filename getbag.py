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
start_time = time.time()
result = mycol.find({"topic": {"$regex": "^/p"}}).limit(1)
print("--- %s seconds --- for reading " % (time.time() - start_time))


redis_client = redis.Redis(host='34.218.26.149', port=6379)

for x in result:
    time = x.get('timestamp')
    y = mycol.find_one(
        {"$and": [{"topic": {"$regex": "^/c"}}, {"timestamp": {"$lt": time}}]}, sort=[("timestamp", -1)])

    print("Generate frame combines ", x.get('topic'), " at timestamp =", x.get(
        'timestamp'), " With ", y.get('topic'), " at timestamp =", y.get('timestamp'))
    values = {x.get('topic'): x.get('message'),
              y.get('topic'): y.get('message')}
    key = str(x.get('bagid')) + '@' + str(x.get('timestamp'))
    print("save in redis as key: " + key)
    redis_client.hmset(key, values)
