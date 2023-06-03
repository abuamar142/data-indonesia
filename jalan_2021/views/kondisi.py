from django.shortcuts import render
from django.http import JsonResponse
from .. models.kondisi import Kondisi

def index(request):
    kondisi = Kondisi()
    data = list(kondisi.all())
    return JsonResponse(data, safe=False)