from django.shortcuts import render
from django.http import JsonResponse
from .. models.jenis import Jenis

def index(request):
    jenis = Jenis()
    data = list(jenis.all())
    return JsonResponse(data, safe=False)