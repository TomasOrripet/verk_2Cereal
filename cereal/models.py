from django.db import models

# Create your models here.
class manufacturer(models.Model):
    manufacturerName = models.CharField(max_length=255)

    def __str__(self):
        return self.manufacturerName

class type(models.Model):
    typeName = models.CharField(max_length=255)

    def __str__(self):
        return self.typeName


class nutritionValue(models.Model):
    nutritionValue = models.CharField(max_length=255)

    def __str__(self):
        return self.nutritionValue


class cereal(models.Model):
    cerealName = models.CharField(max_length=255)
    cerealContents = models.CharField(max_length=255)
    description = models.CharField(max_length=999, null=True)
    amountInStock = models.FloatField()
    price = models.FloatField()
    image = models.CharField(max_length=9999, null=True)
    type = models.ForeignKey(type, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(manufacturer, on_delete=models.CASCADE)
    nutritionValue = models.ForeignKey(nutritionValue, on_delete=models.CASCADE)

    def __str__(self):
        return self.cerealName


