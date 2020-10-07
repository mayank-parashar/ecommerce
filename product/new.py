from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class User(AbstractUser):
    first_name = models.CharField(max_length=64, null=True, blank=False)
    last_name = models.CharField(max_length=64, null=True, blank=False)
    age = models.PositiveIntegerField(null=True)
    mobile_no = models.CharField(max_length=32, null=True, blank=False, db_index=True)
    email = models.EmailField(unique=True)
    class Meta:
        db_index = (['mobile_no', 'email'], ['email'])


def get_users(request, *args, **kwargs):
    all_users = User.objects.all()
    response = UserSerializer(all_users, many=True)
    return Response(response)


def post_user(request, *args, **kwargs):
    user_data = {k: v for k, v in request.data.items()}
    if UserSerializer.validate(user_data):
        user_obj = UserSerializer.save(user_data)
    else:
        return Response(status=HTTP_400_BAD_REQUEST)
    # user_obj = User.object.create(**user_data)
    return Response(data=UserSerializer(user_obj))


def get_user(request, *args, **kwargs):
    identi = request.data.get('identifier')
    if '@' in str(identi):
        user = User.objects.filter(email=identi)
        email_without_domian = identi.split('@')[0]
        user_same_email = User.objects.filter(email__start=email_without_domian)
    else:
        user = User.objects.filter(mobile_no=identi)
    if user.exists():
        return Response(UserSerializer(user_same_email), many=True)

    return Response(HTTP_400_BAD_REQUEST)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'age',
                  'mobile_no',
                  'email')
