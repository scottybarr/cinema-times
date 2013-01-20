from django.db import models

# Create your models here.
class CinemaCompany(models.Model):
    companyId = models.AutoField(primary_key=True, unique=True)
    companyName = models.CharField(max_length=50, unique=True)
    companyWebsite = models.TextField()
    class Admin:
        pass


class Cinema(models.Model):
    cinemaId = models.AutoField(primary_key=True)
    cinemaName = models.CharField(max_length=200, unique=True)
    companyId = models.ForeignKey(CinemaCompany, null=True)
    companyCinemaId = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=15, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    class Admin:
        pass

class Film(models.Model):
    filmId = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    synopsis = models.TextField(null=True)
    length = models.FloatField(null=True)
    rating = models.CharField(max_length=20, null=True)
    director = models.CharField(max_length=40, null=True)
    class Admin:
        pass

class Website(models.Model):
    websiteId = models.AutoField(primary_key=True, unique=True)
    url = models.TextField()
    trackerUrl = models.TextField()
    trackerParams = models.TextField()
    class Admin:
        pass

class VideoType(models.Model):
    videoTypeId = models.AutoField(primary_key=True, unique=True)
    videoDesc = models.TextField(null=True)
    videoType = models.CharField(max_length=20)

class AudioType(models.Model):
    audioTypeId = models.AutoField(primary_key=True, unique=True)
    audioDesc = models.TextField(null=True)
    audioType = models.CharField(max_length=20)

class Schedule(models.Model):
    scheduleId = models.AutoField(primary_key=True, unique=True)
    filmId = models.ForeignKey(Film)
    cinemaId = models.ForeignKey(Cinema)
    filmInternalId = models.CharField(max_length=100,null=True)
    datetime = models.DateTimeField()
    subtitled = models.BooleanField(default=False)
    videoTypeId = models.ForeignKey(VideoType, blank=True)
    audioTypeId = models.ForeignKey(AudioType, blank=True)
    bookingUrl = models.TextField(null=True)
    sessionType = models.CharField(max_length=50, null=True)

class FilmReelLogger(models.Model):
    loggerId = models.AutoField(primary_key=True, unique=True)
    cinemaId = models.ForeignKey(Cinema, blank=True)
    companyId = models.ForeignKey(CinemaCompany, blank=True)
    filmId = models.ForeignKey(Film, blank=True)
    scheduleId = models.ForeignKey(Schedule, blank=True)
    ip = models.CharField(max_length=50)
    dateTime = models.DateTimeField()
    url = models.TextField(blank=True)
