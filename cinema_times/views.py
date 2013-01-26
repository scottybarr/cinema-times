from django.http import HttpResponse
from django.utils import simplejson
from cinema_times.imports.cineworld_cinemas import CineworldImport
from cinema_times import config

def home(request):
    data = simplejson.dumps({'cinemas': []})
    return HttpResponse(data, mimetype='application/json')
