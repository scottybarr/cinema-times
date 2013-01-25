from django.db import models


class Film(models.Model):
    film_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    synopsis = models.TextField(null=True)
    length = models.FloatField(null=True)
    rating = models.CharField(max_length=20, null=True)
    director = models.CharField(max_length=40, null=True)
    class Admin:
        pass
