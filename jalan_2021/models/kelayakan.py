from .connection import db

class Kelayakan:
    def __init__(self):
        self.__collection = db['kelayakan']

    def all(self):
        return self.__collection.find({}, {'_id':0})