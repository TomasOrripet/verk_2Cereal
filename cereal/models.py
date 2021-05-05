from django.db import models

# Create your models here.
class cereal(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    price = models.FloatField()
