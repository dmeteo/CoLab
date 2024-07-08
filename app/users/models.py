from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    surname = models.CharField(blank=False, null=True, verbose_name='Отчество')
    phone_number = models.CharField(blank=False, null=True, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='users_images/', blank=False, null=True, verbose_name='Аватар')
    institute = models.CharField(blank=False, null=True, verbose_name='Институт')
    trend = models.CharField(blank=False, null=True, verbose_name='Направление')
    course = models.SmallIntegerField(blank=False, null=True, verbose_name='Курс')
    bio = models.CharField(blank=False, default='',null=True, verbose_name='О себе, кратко')
    avg_rate = models.CharField(default=0.0, blank=False, null=True, verbose_name='Средняя оценка')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username