from django.db import models
from user.models import ModelBase, Seller


class Product(ModelBase):
    name = models.CharField(max_length=1024, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    mrp = models.FloatField()
    product_seller = models.ManyToManyField(Seller, through="ProductSeller", related_name="actual_product")


class ProductSeller(ModelBase):
    price = models.FloatField()
    quantity = models.IntegerField()
    seller = models.ForeignKey(Seller, related_name="product", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="seller", on_delete=models.CASCADE)


class A(ModelBase):
    name = models.CharField(max_length=256, null=False, blank=True)
    details = models.TextField(null=True, blank=True)
    value = models.IntegerField()


class B(ModelBase):
    name = models.CharField(max_length=256, null=False, blank=True)
    sub = models.CharField(max_length=256, null=False, blank=True)
    a = models.ManyToManyField(A, related_name='b')
