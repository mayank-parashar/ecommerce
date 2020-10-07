from django.db import models

# Create your models here.
from product.models import Product
from user.models import ModelBase, Seller, Customer


class Order(ModelBase):
    PAYMENT_NOT_CONFIRMED = "payment_not_confirmed"
    PAYMENT_FAILED = "payment_failed"
    ORDER_CONFIRM = "order_confirm"
    PACKED = "packed"
    SHIPPED = "shipped"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"

    order_status = (
        (PAYMENT_NOT_CONFIRMED, "PAYMENT_NOT_CONFIRMED"),
        (PAYMENT_FAILED, "PAYMENT_FAILED"),
        (ORDER_CONFIRM, "ORDER_CONFIRM"),
        (PACKED, "PACKED"),
        (SHIPPED, "SHIPPED"),
        (OUT_FOR_DELIVERY, "OUT_FOR_DELIVERY"),
        (DELIVERED, "DELIVERED")
    )

    status = models.CharField(choices=order_status, default=PAYMENT_NOT_CONFIRMED, max_length=128)
    price = models.FloatField()
    seller = models.ForeignKey(Seller, related_name="purchased_item", null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, related_name="order", null=True, on_delete=models.SET_NULL)
    buyer = models.ForeignKey(Customer, related_name="order", on_delete=models.CASCADE)
    quantity = models.IntegerField()
