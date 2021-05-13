from django.db import models
from django.contrib.auth.models import User
from cereal.models import cereal

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=99999, default='https://upload.wikimedia.org/wikipedia/en/0/00/The_Child_aka_Baby_Yoda_%28Star_Wars%29.jpg')
    favorite_cereal = models.ForeignKey(cereal, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return F"{self.profile_image}"