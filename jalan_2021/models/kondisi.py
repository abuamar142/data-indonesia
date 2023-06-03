from .connection import db

class Kondisi:
    def __init__(self):
        self.__collection = db['kondisi']

    def all(self):
        return self.__collection.find({}, {'_id': 0})