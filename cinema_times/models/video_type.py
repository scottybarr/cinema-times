from django.db import models


class VideoType(models.Model):
    video_type_id = models.AutoField(primary_key=True, unique=True)
    video_desc = models.TextField(null=True)
    video_type = models.CharField(max_length=20)
