from django.db import models
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    product = models.CharField(max_length=255)
    expiry_date = models.DateTimeField()
    purchase_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product

    class Meta:
        ordering = ['-expiry_date']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
