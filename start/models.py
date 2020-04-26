from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name