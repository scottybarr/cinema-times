from django.db import models
from film import Film
from cinema import Cinema
from video_type import VideoType
from audio_type import AudioType


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
