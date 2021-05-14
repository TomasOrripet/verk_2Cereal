from django.db import models
from django.contrib.auth.models import User
from cereal.models import cereal
# Create your models here.

class userInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.IntegerField()

class cardInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cardNumber = models.IntegerField(max_length=16)
    nameOfCardholder = models.CharField(max_length=255)
    expirationsDate = models.CharField(max_length=11)
    CVC = models.IntegerField(max_length=3)



