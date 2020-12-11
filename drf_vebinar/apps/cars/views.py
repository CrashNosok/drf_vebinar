from django.shortcuts import render
from rest_framework import generics

# записи могут просатривать только залогиненные пользователи IsAuthenticated
# IsAdminUser - чтобы просматривал только admin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from cars.serializers import CarDetailSerializer, CarsListSerializer
from cars.models import Car

from cars.permissions import IsOwnerOrReadOnly

# авторизация по токену:
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

# для переопределения методов
from rest_framework.response import Response

# если нужна просто форма и не надо, чтобы что-то сохранялось в базу, наследуемся от GenericAPIView
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    # можно переопределить метод
    # def post(self, request):
    #     print(request.data)
    #     return Response({1: 123})


# class CarsListView(generics.ListAPIView):
#     serializer_class = CarsListSerializer
#     # обязательно queryset
#     queryset = Car.objects.all()


class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )


# class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CarDetailSerializer
#     queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()

    # чтобы не повторять эту строчку в каждом классе, смотри settings REST_FRAMEWORK 
    
    # добавим авторизацию по токену (и добавили по сессии):
    # authentication_classes = (TokenAuthentication, SessionAuthentication, )

    # запись может редактировать только тот человек, который эту запись создал
    permission_classes = (IsOwnerOrReadOnly, )
