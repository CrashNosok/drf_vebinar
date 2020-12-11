from rest_framework import serializers
from cars.models import Car

from django.contrib.auth.models import User


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "email"]


class CarsListSerializer(serializers.ModelSerializer):
    # user = AuthorSerializer(many=False, read_only=True)
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # если нужно дополнительное поле:
    # email = serializers.Serializer(label='1234', required=False)
    class Meta:
        model = Car
        # fields = ['...']
        fields = '__all__'
