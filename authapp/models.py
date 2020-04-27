from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CoffeeShop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coffeeshop')
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="coffeeshop_logo", blank=False)

    def __str__(self):
        return self.name


