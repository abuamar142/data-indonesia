from .connection import db

class Jenis:
    def __init__(self):
        self.__collection = db['jenis']
    
    def all(self):
        return self.__collection.find({}, {'_id': 0})