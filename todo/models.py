from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class TodoCard(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    text = models.CharField(max_length=500, verbose_name='Text', blank=True)

    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)

    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    order = models.IntegerField(default=None, null=True, blank=True)

    active_time = models.DateTimeField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    update_time = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.user}'
