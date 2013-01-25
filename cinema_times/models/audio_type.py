from django.db import models


class AudioType(models.Model):
    AudioType_id = models.AutoField(primary_key=True, unique=True)
    audio_desc = models.TextField(null=True)
    AudioType = models.CharField(max_length=20)
