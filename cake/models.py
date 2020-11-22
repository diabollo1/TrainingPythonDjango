from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def posts_for_frontpage(self):
        return self.cake.order_by('-id')[:6]


class Cake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    img = models.ImageField(upload_to="cake", default="cake/default_cake.png")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='cake')

    def __str__(self):
        return self.name

