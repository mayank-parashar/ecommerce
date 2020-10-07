from django.contrib.auth.models import AbstractUser
from django.db import models
from unixtimestampfield import UnixTimeStampField


class ModelBase(models.Model):
    created_on = UnixTimeStampField(auto_now_add=True)
    updated_on = UnixTimeStampField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ActiveModel(ModelBase):
    is_active = models.BooleanField(default=True)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
        abstract = True


class User(AbstractUser):
    # COMMON = "common"
    # PRIME = "prime"
    # USER_TYPES = (
    #     (COMMON, "COMMON"),
    #     (PRIME, "PRIME")
    # )
    user_name = None
    # user_type = models.CharField(choices=USER_TYPES, max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Seller(ModelBase):
    user = models.OneToOneField(User, related_name='seller', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=256, blank=True)


class Customer(ModelBase):
    user = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=256, blank=True)


