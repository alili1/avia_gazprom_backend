
from django.shortcuts import render
from rest_framework import generics
from avia_api.models import City
from avia_api.serializers import CitySerializer


class CityView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
