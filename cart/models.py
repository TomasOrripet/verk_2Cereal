from django.db import models
from django.contrib.auth.models import User
from cereal.models import cereal
# Create your models here.

class order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField( null=True, blank=True)
    trasnaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    def get_cart_total(self):
        orderItems = self.ordercerealitem_set.all()
        total = sum([cereal.get_total for cereal in orderItems])
        return total
    def get_cart_items(self):
        orderItems = self.ordercerealitem_set.all()
        total = sum([cereal.get_total for cereal in orderItems])
        return total

class orderCerealItem(models.Model):
    cereal = models.ForeignKey(cereal, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    def get_total(self):
        total = self.product.price * self.quantity
        return total

class userCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    cereal = models.ForeignKey(cereal, on_delete=models.SET_NULL, blank=True, null=True)


