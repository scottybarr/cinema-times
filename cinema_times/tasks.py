from cinema_times.imports.cineworld_cinemas import CineworldImport
from cinema_times import config

def import_cinemas():
    CineworldImport(config)
