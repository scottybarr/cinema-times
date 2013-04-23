from django.http import HttpResponse
from django.utils import simplejson

from cinema_times import config
from cinema_times.imports.cineworld.cineworld_cinemas import CineworldCinemas
from cinema_times.imports.cineworld.cineworld_schedule import CineworldSchedule

__author__ = 'scott'

def import_cineworld_cinemas(request):
    s = CineworldCinemas(config).parse_cinemas()
    return HttpResponse(simplejson.dumps(s), mimetype='application/json')


def import_cineworld_schedule(request):
    s = CineworldSchedule().get_sched()
    return HttpResponse(simplejson.dumps(s), mimetype='application/json')