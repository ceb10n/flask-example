import pymongo
import os

mongo_name = os.environ.get("mlab_db")
mongo_port = os.environ.get("mlab_prt")
mongo_src = os.environ.get("mlab_src")
mongo_usr = os.environ.get("mlab_usr")
mongo_pwd = os.environ.get("mlab_pwd")

connection = pymongo.MongoClient(mongo_src, int(mongo_port))
db = connection[mongo_name]
db.authenticate(mongo_usr, mongo_pwd)
