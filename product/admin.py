from django.contrib import admin

# Register your models here.
from product.models import Product, ProductSeller, A, B


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductSeller)
class ProductSellerAdmin(admin.ModelAdmin):
    pass


@admin.register(A)
class AAdmin(admin.ModelAdmin):
    pass


@admin.register(B)
class BAdmin(admin.ModelAdmin):
    pass