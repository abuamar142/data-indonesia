from django.shortcuts import render
from django.http import JsonResponse
from .. models.kelayakan import Kelayakan
from .. models.utils import Merge


def index(request):
    query = {}
    search = request.GET.get('search')
    if search:
        query = {'Provinsi': {'$regex': search, '$options': 'i'}}
    data = Merge().all(query)
    return render(request, 'kelayakan.html', {'data': data})