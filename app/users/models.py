from django.db import models
from django.contrib.auth.models import AbstractUser

from app.projects.models import Project

class User(AbstractUser):
    surname = models.CharField(blank=False, null=True, verbose_name='Отчество')
    phone_number = models.CharField(blank=False, null=True, verbose_name='Номер телефона')
    image = models.ImageField(upload_to='users_images', blank=False, null=True, verbose_name='Аватар')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username