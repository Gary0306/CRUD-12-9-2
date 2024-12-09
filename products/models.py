from django.db import models


class Product(models.Model):
    title = models.CharField(null=True, max_length=100)
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
