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
        return self.name

