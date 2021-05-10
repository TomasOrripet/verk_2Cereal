from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class createAccount(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.IntegerField()


class createAccountImage(models.Model):
    image = models.CharField(max_length=99999, null=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE)


class userAndPassword(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    account = models.ForeignKey(createAccount, on_delete=models.CASCADE)

