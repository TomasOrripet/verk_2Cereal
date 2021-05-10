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
    type = models.ForeignKey(createType, on_delete=models.CASCADE)

    def __str__(self):
        return self.cerealName

class cerealImage(models.Model):
    image = models.CharField(max_length=9999)
    cereal = models.ForeignKey(createCereal, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
