from django.contrib.auth.models import AbstractUser
from django.db import models


class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()


class User(AbstractUser):
    location = models.CharField(max_length=64)
    mobile_no = models.CharField(max_length=16)


class Customer(User):
    pass


class HallOwner(User):
    pass


class Movie(ModelBase):
    name = models.CharField(max_length=256)


class CinemaHall(ModelBase):
    name =models.CharField(max_length=256)


class Screen(ModelBase):
    name = models.CharField(max_length=256)
    hall = models.ForeignKey(CinemaHall, related_name='screen', on_delete=models.CASCADE)
    movie = models.ManyToManyField(Movie, through="MovieScreen")


class MovieScreen(ModelBase):
    price = models.PositiveIntegerField(null=True, blank=False)
    movie = models.ForeignKey(Movie, related_name='screens', on_delete=models.SET_NULL)
    screen = models.ForeignKey(Screen, related_name='movies', on_delete=models.SET_NULL)





