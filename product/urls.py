from django.urls import path, include
from rest_framework import routers

from product.views import ProductView

router = routers.DefaultRouter()
router.register("", ProductView)

urlpatterns = [
    path('', include(router.urls))
]