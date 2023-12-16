from django.db import models


class City(models.Model):
    city_name = models.CharField(null=False, max_length=256)
    country = models.CharField(null=False, max_length=50)
    airport_code = models.BigIntegerField(null=False)

