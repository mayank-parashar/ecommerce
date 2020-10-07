from django.contrib import admin
# Register your models here.
from user.models import User, Seller, Customer


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Seller)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    pass


