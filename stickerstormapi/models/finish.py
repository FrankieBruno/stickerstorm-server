from django.db import models

class Finish(models.Model):
    finish_type = models.CharField(max_length=55)