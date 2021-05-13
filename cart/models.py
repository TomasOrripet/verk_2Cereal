from django.db import models
from django.contrib.auth.models import User
from cereal.models import cereal
# Create your models here.
class userCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    cereal = models.ForeignKey(cereal, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=1, blank=True)



    def __str__(self):
        return f"{self.cereal_id}"

