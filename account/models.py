from django.db import models
from django.contrib.auth.models import User
from cereal.models import cereal

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=99999)
    favorite_cereal = models.ForeignKey(cereal, on_delete=models.CASCADE)


