from django.db import models

# Create your models here.
class Cereal(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    price = models.FloatField()
