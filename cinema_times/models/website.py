from django.db import models


class Website(models.Model):
    website_id = models.AutoField(primary_key=True, unique=True)
    url = models.TextField()
    tracker_url = models.TextField()
    tracker_params = models.TextField()

    class Admin:
        pass

    class Meta:
        app_label = 'cinema_times'
