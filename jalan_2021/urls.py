from django.urls import path

from . views.jenis import index as jenis_index
from . views.kelayakan import index as kelayakan_index

urlpatterns = [
    path('jenis', jenis_index, name='jenis_index'),
    path('kelayakan', kelayakan_index, name='kelayakan_index')
]