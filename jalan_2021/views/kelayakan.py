from django.shortcuts import render
from django.http import JsonResponse
from .. models.kelayakan import Kelayakan

def index(request):
    kelayakan = Kelayakan()
    data = list(kelayakan.all())
    return render(request, 'kelayakan.html', {'data': data})