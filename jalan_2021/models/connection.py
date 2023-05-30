import pymongo

mongo = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo['Data_jalan']