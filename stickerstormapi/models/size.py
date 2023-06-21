from django.db import models


class Size(models.Model):
    sticker_size = models.IntegerField()