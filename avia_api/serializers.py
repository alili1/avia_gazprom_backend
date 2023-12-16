from rest_framework import serializers

from avia_api.models import City, Flight


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city_name', 'country', 'airport_code')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'source', 'destination', 'date_of_journey', 'price')