from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from user.Serializers import UserSerializer
from user.models import User


class UserView(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        print(request.user)

