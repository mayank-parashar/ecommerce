from django.db import transaction
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
# Create your views here.
from parking.Serializers import ParkingTypeSerializer, BookingSerializer
from parking.models import ParkingType, Place, Booking, Vehicle, Transaction
import datetime
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet


class BookingView(ViewSet):
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['get'], url_path='available')
    def empty_parking(self, request, *args, **kwargs):
        type = request.GET.get('slot_type')
        parking_slots = ParkingType.objects.prefetch_related('place').filter(type=type, place__status=Place.EMPTY)
        count = parking_slots[0].place.count() if parking_slots.count() > 0 else 0
        slot = parking_slots[0].place.all()[0].id if count > 0 else None
        return Response({"slot": slot, "count": count})

    @action(detail=False, methods=['post'], url_path='book')
    def book_place(self, request):
        place_id = request.data.get('place_id')
        vehicle_no = request.data.get('vehicle_no')
        vehicle_type = request.data.get('vehicle_type')
        vehicle_already_parked = Booking.objects.filter(vehicle__no=vehicle_no, status=Booking.IN_PROGRESS).exists()
        if vehicle_already_parked:
            return Response(status=HTTP_400_BAD_REQUEST, data={"msg": "Vehicle no. is redundant"})
        place = Place.objects.filter(id=place_id).select_related('type')
        place = place.first()
        if place:
            with transaction.atomic():
                if place.type.type != vehicle_type:
                    raise Exception("Invalid slot selected")
                place.status = Place.BOOKED
                booking = Booking.objects.create(place=place, start_time=datetime.datetime.now())
                vehicle = Vehicle.objects.create(no=vehicle_no, type=vehicle_type)
                booking.vehicle = vehicle
                place.save()
                booking.save()

                return Response({"booking_id": booking.id})
        else:
            Response(status=HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='complete')
    def complete_booking(self, request):
        vehicle_no = request.data.get('vehicle_no')
        # check_booking_exist with this vehicle
        booking = Booking.objects.filter(vehicle__no=vehicle_no, status=Booking.IN_PROGRESS). \
            select_related('vehicle', 'place').first()
        if booking:
            with transaction.atomic():
                booking.status = Booking.COMPLETED
                vehicle = booking.vehicle
                price = ParkingType.objects.values_list("pricing", flat=True).filter(type=vehicle.type)[0]
                start_time = booking.start_time
                booking.end_time = datetime.datetime.now()
                total_amount = price * ((datetime.datetime.now() - start_time.replace(tzinfo=None)).seconds / 3600)
                place = booking.place
                place.status = Place.EMPTY
                transaction_object = Transaction.objects.create(amount=total_amount)
                booking.transaction = transaction_object
                booking.save()
                place.save()
                return Response(data={'amount': total_amount})
        else:
            return Response(status=HTTP_400_BAD_REQUEST, data="Invalid vehicle")


class ParkingTypeView(ModelViewSet):
    queryset = ParkingType.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ParkingTypeSerializer


class BookingDataView(ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = BookingSerializer
