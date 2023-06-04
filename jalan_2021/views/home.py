from django.shortcuts import render
from .. models.utils import Merge

def home(request):
    query = {}
    search = request.GET.get('search')
    if search:
        query = {'Provinsi': {'$regex': search, '$options': 'i'}}
    data = Merge().all(query)
    return render(request, 'index.html', {'data': data})

def team(request):
    return render(request, 'team.html')