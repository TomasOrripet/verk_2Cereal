from django.db import models
from cereal.models import manufacturer


class toys(models.Model):
    toyName = models.CharField(max_length=255)
    description = models.CharField(max_length=999, null=True)
    price = models.FloatField()
    amountInStock = models.FloatField()
    type = models.CharField(max_length=255)
    image = models.CharField(max_length=99999, null=True)
    manufacturer = models.ForeignKey(manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.toyName
