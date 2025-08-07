from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer
from .models import CityModel

@api_view(['GET'])
def CityList(request):
    cities = CityModel.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CityCreate(request):
    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def CityDetail(request, id):
    city = CityModel.objects.get(id=id)
    serializer = CitySerializer(city)
    return Response(serializer.data)


@api_view(['PUT'])
def CityUpdate(request, id):
    city = CityModel.objects.get(id=id)
    serializer = CitySerializer(instance=city, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def CityDelete(request, id):
    city = CityModel.objects.get(id=id)
    city.delete()
    return Response("City deleted")