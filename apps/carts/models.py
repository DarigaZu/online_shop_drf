from django.db import models

from django.contrib.auth import get_user_model

from apps.products.models import Product
from apps.orders.models import Order



User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.user.username
    

class CartItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )
    quantity = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return f'{self.product.title} - {self.quantity}'