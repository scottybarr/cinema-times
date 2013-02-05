from django.db import models


# Create your models here.
class CinemaCompany(models.Model):
    company_id = models.AutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=50, unique=True)
    company_website = models.TextField()

    class Admin:
        pass

    class Meta:
        app_label = 'cinema_times'
