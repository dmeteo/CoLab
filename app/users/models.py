from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    surname = models.CharField(blank=False, null=False, verbose_name='Отчество')
    phone_number = models.CharField(blank=False, null=False, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='users_images', blank=False, null=False, verbose_name='Аватар')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username