from django.db import models

# Create your models here.
class createType(models.Model):
    typeName = models.CharField(max_length=255)

    def __str__(self):
        return self.typeName



class createCereal(models.Model):
    cerealName = models.CharField(max_length=255)
    cerealNutritionalValue = models.CharField(max_length=255)
    cerealContents = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=9999, null=True)
    type = models.ForeignKey(createType, on_delete=models.CASCADE)

    def __str__(self):
        return self.cerealName


