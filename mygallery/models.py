from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    