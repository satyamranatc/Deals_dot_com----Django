from rest_framework.serializers import ModelSerializer
from .models import PropertyModel

from City.serializers import CitySerializer

class PropertySerializer(ModelSerializer):
    propertyCity = CitySerializer()
    class Meta:
        model = PropertyModel
        fields = '__all__'
