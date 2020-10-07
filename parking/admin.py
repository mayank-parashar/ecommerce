from django.contrib import admin

# Register your models here.
from parking.models import ParkingType, Place, Vehicle, Transaction, Booking


@admin.register(ParkingType)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicle)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class ProductAdmin(admin.ModelAdmin):
    pass