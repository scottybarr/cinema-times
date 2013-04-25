from cinema_times import config
from cinema_times.imports.cineworld.cineworld_cinemas import CineworldCinemas
from cinema_times.imports.cineworld.cineworld_schedule import CineworldSchedule
from cinema_times.models import Cinema, Schedule
from django.http import HttpResponse
from django.utils import simplejson


def home(request):
    return HttpResponse(simplejson.dumps({}), mimetype='application/json')


def cinema_locations(request):
    cinema_list = Cinema.objects.all()
    cinemas = {
        str(c.cinema_id): {
            'name': c.cinema_name,
            'address': c.address,
            'phone': c.phone,
            'longitude': c.longitude,
            'latitude': c.latitude
        }
        for c in cinema_list
    }
    return HttpResponse(simplejson.dumps(cinemas), mimetype='application/json')
