from rest_framework.serializers import ModelSerializer
from .models import CityModel
# from Property.serializers import PropertySerializer

class CitySerializer(ModelSerializer):
    # properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = CityModel
        fields = '__all__'
