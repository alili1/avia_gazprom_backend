from django.contrib import admin
from django.urls import path
from avia_api.views import CityView

urlpatterns = [
    path('getCityList', CityView.as_view())
]