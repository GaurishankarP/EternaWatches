from django.db import models
from django.contrib.auth.models import User   # <-- import User

class Watch(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="watches",
        null=True,       # temp so old rows won’t break
        blank=True
    )
    image = models.ImageField(upload_to="media", null=True, blank=True)
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    strap_material = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.name}"
