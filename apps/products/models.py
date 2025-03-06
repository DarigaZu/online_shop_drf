from django.db import models

from django.contrib.auth import get_user_model

from apps.categories.models import Category



User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
    )
    image = models.ImageField(
        upload_to='products/'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.CASCADE,
        related_name='products'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'