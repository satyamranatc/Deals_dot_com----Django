from django.db import models

class CityModel(models.Model):
    cityName = models.CharField(max_length=50)
    cityPoster = models.CharField(max_length=500)
    total_properties = models.IntegerField(default=0)
    def __str__(self):
        return self.cityName