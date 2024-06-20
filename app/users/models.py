from django.db import models
from django.contrib.auth.models import AbstractUser

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
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    institute = models.CharField(blank=False, null=True, verbose_name='Институт')
    trend = models.CharField(blank=False, null=True, verbose_name='Направление')
    course = models.SmallIntegerField(blank=False, null=True, verbose_name='Курс')
    bio = models.CharField(blank=False, null=True, verbose_name='О себе, кратко')

    def __str__(self):
        return str(self.user)
