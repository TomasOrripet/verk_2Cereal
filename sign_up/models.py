from django.db import models


# Create your models here.

class createAccount(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.IntegerField()


class createAccountImage(models.Model):
    image = models.CharField(max_length=9999)
    account = models.ForeignKey(createAccount, on_delete=models.CASCADE)
