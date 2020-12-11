from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Car(models.Model):
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
    )
    vin = models.CharField(max_length=64, verbose_name='Vin', unique=True, db_index=True)
    color = models.CharField(max_length=64, verbose_name='Color')
    brand = models.CharField(max_length=64, verbose_name='Brand')
    car_type = models.IntegerField(choices=CAR_TYPES, verbose_name='Car_Type')
    # related_name=...
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
