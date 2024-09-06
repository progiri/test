from django.db import models

from accounts.models import User


class Task(models.Model):
    STATUS_CHOICES = (
        (0, 'В процессе'),
        (1, 'Выполнено'),
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



