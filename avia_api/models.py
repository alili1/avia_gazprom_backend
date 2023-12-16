from django.db import models


class City(models.Model):
    city_name = models.CharField(null=False, max_length=256)
    country = models.CharField(null=False, max_length=50)
    airport_code = models.IntegerField(null=False)

class Flight(models.Model):
    airline = models.IntegerField(null=False)
    date_of_journey = models.DateField(null=False)
    source = models.IntegerField(null=False)
    destination = models.IntegerField(null=False)
    additional_info = models.CharField(null=False, max_length=256)
    price = models.IntegerField(null=False)
    data_source = models.CharField(null=False, max_length=256)