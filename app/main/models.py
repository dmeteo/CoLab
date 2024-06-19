from django.db import models
from django.urls import reverse

class MyModelName(models.Model):
    """Типичный класс модели, производный от класса Model."""

    # Поля
    my_field_name = models.CharField(max_length=20, help_text='Введите описание поля')
    # …

    # Метаданные
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к определенному экземпляру MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return self.my_field_name
