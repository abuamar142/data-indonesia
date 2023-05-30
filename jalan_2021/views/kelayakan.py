from django.shortcuts import render
from django.http import JsonResponse
from .. models.kelayakan import Kelayakan

def index(request):
    kelayakan = Kelayakan()
    data = list(kelayakan.all())
    return JsonResponse(data, safe=False)