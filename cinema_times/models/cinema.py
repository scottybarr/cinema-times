from django.db import models
from cinema_times.models.cinema_company import CinemaCompany


class Cinema(models.Model):
    cinema_id = models.AutoField(primary_key=True)
    cinema_name = models.CharField(max_length=200, unique=True)
    company = models.ForeignKey(CinemaCompany, null=True)
    company_cinema_id = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=15, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    class Admin:
        pass

    class Meta:
        app_label = 'cinema_times'
