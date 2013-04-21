from django.db import models
from cinema_times.models.film import Film
from cinema_times.models.cinema import Cinema
from cinema_times.models.video_type import VideoType
from cinema_times.models.audio_type import AudioType


class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True, unique=True)
    film_id = models.ForeignKey(Film)
    cinema_id = models.ForeignKey(Cinema)
    film_internal_id = models.CharField(max_length=100,null=True)
    datetime = models.DateTimeField()
    subtitled = models.BooleanField(default=False)
    video_type_id = models.ForeignKey(VideoType, blank=True)
    audio_type_id = models.ForeignKey(AudioType, blank=True)
    booking_url = models.TextField(null=True)
    session_type = models.CharField(max_length=50, null=True)

    class Meta:
        app_label = 'cinema_times'
