from django.db import models


class Watch(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    strap_material = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.IntegerField()
