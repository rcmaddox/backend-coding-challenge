from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


    @property
    def full_name(self):
        return f"{self.name}, {self.state}, {self.country}"

