
from django.shortcuts import render
from rest_framework import generics
from avia_api.models import City, Flight
from avia_api.serializers import CitySerializer, FlightSerializer


class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class FlightView(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer