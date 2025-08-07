from django.db import models

from City.models import CityModel

# Create your models here.
class PropertyModel(models.Model):
    propertyName = models.CharField(max_length=50)
    propertyPoster = models.CharField(max_length=500)
    propertyDescription = models.CharField(max_length=500)
    propertyPrice = models.IntegerField(default=0)
    PROPERTY_TYPE_CHOICES = [
    ("Villa", "Villa"),
    ("Apartment", "Apartment"),
    ("House", "House"),
]
    propertyType = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES),
    propertySize = models.IntegerField(default=500)
    propertyCity = models.ForeignKey("City.CityModel", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.propertyName
    