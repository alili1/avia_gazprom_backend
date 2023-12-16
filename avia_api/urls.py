from django.contrib import admin
from django.urls import path
from avia_api.views import CityView, FlightView

urlpatterns = [
    path('getCityList', CityView.as_view()),
    path('getFlightsList', FlightView.as_view())
]