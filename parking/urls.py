from django.urls import path, include
from rest_framework import routers

from parking.models import Booking
from parking.views import BookingView, ParkingTypeView, BookingDataView

router = routers.DefaultRouter()
router.register("", BookingView, basename="booking")
router.register("parkingtype", ParkingTypeView, basename="parkingtype")
router.register("booking", BookingDataView, basename="Booking_data")


urlpatterns = [
    path('', include(router.urls))
]