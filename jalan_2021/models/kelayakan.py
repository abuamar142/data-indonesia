from .connection import db

class Kelayakan:
    def __init__(self):
        self.__collection = db['kelayakan']

    def all(self, query={}):
        return self.__collection.find(query, {'_id': 0, 'Kd_Prov': 1, 'Provinsi': 1, 'Mantap_km': 1, 'Mantap_percent': '$Mantap_%', 'TMantap_km': 1, 'TMantap_percent': '$TMantap_%'})