from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='https://www.google.com/search?q=faceless+profile+picture&safe=strict&sxsrf=ALeKk03ue3aAtf8dlDatKzVutVIYtKvwbQ:1620736625771&tbm=isch&source=iu&ictx=1&fir=AymqgxEoSzzyvM%252Ca7Wkb6mAFYRy3M%252C_&vet=1&usg=AI4_-kSdzLngLoiPj7KGMlqQYZ--2qEJ-g&sa=X&ved=2ahUKEwiL4Om20sHwAhWOY8AKHVcUDSUQ9QF6BAgVEAE#imgrc=AymqgxEoSzzyvM', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
