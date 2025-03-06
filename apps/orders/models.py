from django.db import models

from django.contrib.auth import get_user_model



User = get_user_model()


class Address(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    street = models.CharField(
        max_length=50
    )
    city = models.CharField(
        max_length=20
    )
    zip_code = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f'{self.street}, {self.city}, {self.zip_code}'

class PaymentMethod(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    method = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.method


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        default=1
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'В ожидании'),
            ('completed', 'Завершен'),
            ('canceled', 'Отменен')       
        ],
        default='pending'
    )

    
    def total_cost(self):
        total = sum(
            item.product.price * item.quantity
            for item in self.items.all()
        )
        return total


    def __str__(self):
        return f'Заказ от {self.user.username}'
    

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'