from .connection import db

class Jenis:
    def __init__(self):
        self.__collection = db['jenis']
    
    def all(self, query={}):
        return self.__collection.find(query, {'_id': 0, 'Kd_Prov': 1, 'Provinsi': 1, 'Paved': 1, 'Paved_percent': '$Paved_%', 'UnPaved': 1, 'UnPaved_percent': '$UnPaved_%'})