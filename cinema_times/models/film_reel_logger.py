from django.db import models
from cinema import Cinema
from cinema_company import CinemaCompany
from film import Film
from schedule import Schedule


class FilmReelLogger(models.Model):
    logger_id = models.AutoField(primary_key=True, unique=True)
    cinema_id = models.ForeignKey(Cinema, blank=True)
    company_id = models.ForeignKey(CinemaCompany, blank=True)
    film_id = models.ForeignKey(Film, blank=True)
    schedule_id = models.ForeignKey(Schedule, blank=True)
    ip = models.CharField(max_length=50)
    dateTime = models.DateTimeField()
    url = models.TextField(blank=True)
