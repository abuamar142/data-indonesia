from django.urls import path

from . views.jenis import index as jenis_index

urlpatterns = [
    path('jenis', jenis_index, name='jenis_index')
]