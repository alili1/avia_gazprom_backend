from rest_framework import serializers

from avia_api.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'city_name', 'country', 'airport_code')
