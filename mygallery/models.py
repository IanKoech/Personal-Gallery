from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model);
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update()