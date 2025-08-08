from rest_framework.serializers import ModelSerializer
from .models import CityModel

class CitySerializer(ModelSerializer):

    class Meta:
        model = CityModel
        fields = '__all__'
