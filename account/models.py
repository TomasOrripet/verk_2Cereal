from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    image = models.ImageField(default='https://miro.medium.com/max/2400/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg', upload_to='account/profile_pics')
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} Profile'
