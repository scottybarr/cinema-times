from django.db import models

# Create your models here.
class CinemaCompany(models.Model):
    company_id = models.AutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=50, unique=True)
    company_website = models.TextField()
    class Admin:
        pass


class Cinema(models.Model):
    cinema_id = models.AutoField(primary_key=True)
    cinema_name = models.CharField(max_length=200, unique=True)
    company_id = models.ForeignKey(CinemaCompany, null=True)
    company_cinema_id = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=15, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    class Admin:
        pass

class Film(models.Model):
    film_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    synopsis = models.TextField(null=True)
    length = models.FloatField(null=True)
    rating = models.CharField(max_length=20, null=True)
    director = models.CharField(max_length=40, null=True)
    class Admin:
        pass

class Website(models.Model):
    website_id = models.AutoField(primary_key=True, unique=True)
    url = models.TextField()
    tracker_url = models.TextField()
    tracker_params = models.TextField()
    class Admin:
        pass

class VideoType(models.Model):
    video_type_id = models.AutoField(primary_key=True, unique=True)
    video_desc = models.TextField(null=True)
    video_type = models.CharField(max_length=20)

class AudioType(models.Model):
    AudioType_id = models.AutoField(primary_key=True, unique=True)
    audio_desc = models.TextField(null=True)
    AudioType = models.CharField(max_length=20)

class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True, unique=True)
    film_id = models.ForeignKey(Film)
    cinema_id = models.ForeignKey(Cinema)
    film_internal_id = models.CharField(max_length=100,null=True)
    datetime = models.DateTimeField()
    subtitled = models.BooleanField(default=False)
    video_type_id = models.ForeignKey(VideoType, blank=True)
    AudioType_id = models.ForeignKey(AudioType, blank=True)
    booking_url = models.TextField(null=True)
    session_type = models.CharField(max_length=50, null=True)

class FilmReelLogger(models.Model):
    logger_id = models.AutoField(primary_key=True, unique=True)
    cinema_id = models.ForeignKey(Cinema, blank=True)
    company_id = models.ForeignKey(CinemaCompany, blank=True)
    film_id = models.ForeignKey(Film, blank=True)
    schedule_id = models.ForeignKey(Schedule, blank=True)
    ip = models.CharField(max_length=50)
    dateTime = models.DateTimeField()
    url = models.TextField(blank=True)
