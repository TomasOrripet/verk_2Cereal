from django.db import models
from django.contrib.auth.models import User
from cereal.models import cereal
from toys.models import toys
# Create your models here.
class userCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    cereal = models.ForeignKey(cereal, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True)
    price = models.FloatField(blank=True, null=True)


    def __str__(self):
        return f"{self.quantity}"

class toyCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    toy = models.ForeignKey(toys, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True)
    price = models.FloatField(blank=True, null=True)


    def __str__(self):
        return f"{self.quantity}"

