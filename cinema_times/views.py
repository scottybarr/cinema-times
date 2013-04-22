from cinema_times import config
from cinema_times.imports.cineworld_cinemas import CineworldCinemas
from cinema_times.imports.cineworld_schedule import CineworldSchedule
from cinema_times.models import Cinema
from django.http import HttpResponse
from django.utils import simplejson


def home(request):
    return HttpResponse(simplejson.dumps({}), mimetype='application/json')


def import_cineworld_schedule(request):
    s = CineworldCinemas(config).parse_cinemas()
    return HttpResponse(simplejson.dumps(s), mimetype='application/json')


def import_cineworld_schedule(request):
    s = CineworldSchedule().get_sched()
    return HttpResponse(simplejson.dumps(s), mimetype='application/json')


def cinema_locations(request):
    cinemas = {
        str(c.cinema_id): {
            'name': c.cinema_name,
            'address': c.address,
            'phone': c.phone,
            'longitude': c.longitude,
            'latitude': c.latitude
        }
        for c in Cinema.objects.filter()
    }
    return HttpResponse(simplejson.dumps(cinemas), mimetype='application/json')
