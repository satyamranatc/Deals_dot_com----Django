# In Property/serializers.py
from rest_framework.serializers import ModelSerializer
from .models import PropertyModel
from City.serializers import CitySerializer

class PropertySerializer(ModelSerializer):
    class Meta:
        model = PropertyModel
        fields = '__all__'

class PropertyDetailSerializer(ModelSerializer):
    propertyCity = CitySerializer(read_only=True)
    class Meta:
        model = PropertyModel
        fields = '__all__'