from django.urls import path

from . views.jenis import index as jenis_index
from . views.kelayakan import index as kelayakan_index
from . views.kondisi import index as kondisi_index
from . views.home import home, team

urlpatterns = [
    path('', home, name='home'),
    path('team', team, name='team'),
    path('jenis', jenis_index, name='jenis_index'),
    path('kelayakan', kelayakan_index, name='kelayakan_index'),
    path('kondisi', kondisi_index, name='kondisi_index')
]