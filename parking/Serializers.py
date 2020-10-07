from rest_framework import serializers
from parking.models import ParkingType, Booking


class ParkingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingType
        exclude = ('id', )


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ('id', )