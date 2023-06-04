from .connection import db

class Kondisi:
    def __init__(self):
        self.__collection = db['kondisi']

    def all(self, query={}):
        return self.__collection.find(query, {'_id': 0, 'Kd_Prov': 1, 'Provinsi': 1, 'Kondisi_Baik': 1, 'Baik_percent': '$Baik_%', 'Kondisi_Sedang': 1, 'Sedang_percent': '$Sedang_%'})