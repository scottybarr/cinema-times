from celery import task
from celery.schedules import crontab
from cinema_times.imports.cineworld_cinemas import CineworldImport
from cinema_times import config

@task.periodic_task(run_every=crontab(hour=10, minute=0, day_of_week="mon"))
def import_cinemas():
    CineworldImport(config)
