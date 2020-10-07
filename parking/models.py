from django.db import models
import datetime


# Create your models here.

class ParkingType(models.Model):
    type = models.CharField(max_length=64)
    pricing = models.IntegerField()


class Place(models.Model):
    EMPTY = "empty"
    BOOKED = "booked"
    parking_status = ((EMPTY, "EMPTY"),
                      (BOOKED, "BOOKED")
                      )
    no = models.IntegerField()
    status = models.CharField(max_length=32, choices=parking_status, default=EMPTY)
    type = models.ForeignKey(ParkingType, related_name="place", on_delete=models.CASCADE)


class Vehicle(models.Model):
    no = models.CharField(max_length=32, null=True, blank=True)
    type = models.CharField(max_length=32, null=True, blank=True)


class Transaction(models.Model):
    amount = models.IntegerField(null=True, blank=True)


class Booking(models.Model):
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"
    booking_status = (
        (IN_PROGRESS, "IN_PROGRESS"),
        (COMPLETED, "COMPLETED")
    )
    status = models.CharField(max_length=32, choices=booking_status, default=IN_PROGRESS)
    vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True)
    transaction = models.OneToOneField(Transaction, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)





