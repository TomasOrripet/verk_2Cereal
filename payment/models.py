from django.db import models
from django.contrib.auth.models import User
from cereal.models import cereal
# Create your models here.

class userInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.IntegerField()

class cardInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cardNumber = models.IntegerField(default=0)
    nameOfCardholder = models.CharField(max_length=255)
    expirationsDate = models.DateField()
    CVC = models.IntegerField()



