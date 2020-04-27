from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, default="")
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.brand} {self.name}'



class Tea(models.Model):
    Black = "Черный"
    Green = "Зеленый"
    Fruit = "Фруктовый"
    TYPE_TEA_CHOICES = (
        (Black, 'Черный'),
        (Green, "Зеленый"),
        (Fruit, "Фруктовый"),
    )
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, default="")
    type_choice = models.CharField(max_length=30, choices=TYPE_TEA_CHOICES)
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return f'{self.brand} {self.name}'

class Order(models.Model):
    order_name = models.ForeignKey(Coffee)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
