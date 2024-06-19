from django.db import models

from config import settings


class Project(models.Model):
    name = models.CharField(verbose_name="Название проекта")
    about = models.TextField(verbose_name="О проекте")
    rating = models.IntegerField(default=0, null=True, blank=True, verbose_name="Оценка за проект")

    def __str__(self):
        return self.name
    
class UserInProject(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class MemberProject(models.Model):
    name = models.ForeignKey(UserInProject, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(null=True, blank=True, verbose_name="Роль")
    rate = models.FloatField(default=0, null=True, blank=True, verbose_name='Оценка')
    text = models.TextField(null=True, blank=True)