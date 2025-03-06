from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    description = models.TextField(
        blank=True
    )


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )    
    name = models.CharField(
        max_length=20
    )


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'