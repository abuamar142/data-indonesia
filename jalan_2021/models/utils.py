from .jenis import Jenis
from .kelayakan import Kelayakan
from .kondisi import Kondisi

class Merge:
    def __init__(self):
        self.jenis = Jenis()
        self.kelayakan = Kelayakan()
        self.kondisi = Kondisi()
    
    def all(self, query={}):
        merged_data = {}

        for source in [self.jenis.all(query), self.kelayakan.all(query), self.kondisi.all(query)]:
          for item in source:
              kd = item['Kd_Prov']
              if kd in merged_data:
                  merged_data[kd].update(item)
              else:
                  merged_data[kd] = item
        
        return list(merged_data.values())