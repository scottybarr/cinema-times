from django.http import HttpResponse
from cinema_times.imports.cineworld_cinemas import CineworldImport
from cinema_times import config

def home(request):
    return HttpResponse("Hello, world. You're at the poll index.")
