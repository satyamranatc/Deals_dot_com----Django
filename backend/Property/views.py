from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PropertySerializer
from .serializers import PropertyDetailSerializer

from .models import PropertyModel

from City.serializers import CitySerializer
from City.models import CityModel


@api_view(['GET'])
def PropertyList(request):
    properties = PropertyModel.objects.all()
    serializer = PropertyDetailSerializer(properties, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PropertyDetail(request, id):
    property = PropertyModel.objects.get(id=id)
    serializer = PropertySerializer(property)
   
    return Response(serializer.data)


@api_view(['POST'])
def PropertyCreate(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        property_instance = serializer.save()  # Save property

        # Get the related city
        if property_instance.propertyCity:
            city = property_instance.propertyCity
            print(city)
            city.total_properties += 1
            city.save()  # Save the updated city

        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['PUT'])
def PropertyUpdate(request, id):
    property = PropertyModel.objects.get(id=id)
    serializer = PropertySerializer(instance=property, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def PropertyDelete(request, id):
    property_instance = PropertyModel.objects.get(id=id)
    if property_instance.propertyCity:
            city = property_instance.propertyCity
            print(city)
            city.total_properties -= 1
            city.save()  # Save the up
    property_instance.delete()
    return Response("Property deleted")
