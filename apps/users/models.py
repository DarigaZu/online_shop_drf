from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(
        upload_to='users/',
        verbose_name='Аватарка',
        null=True,
        blank=True
    )
    bio = models.TextField(
        verbose_name='Био',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.username
    

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
