# Generated by Django 3.2 on 2021-05-11 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='https://www.google.com/search?q=faceless+profile+picture&safe=strict&sxsrf=ALeKk03ue3aAtf8dlDatKzVutVIYtKvwbQ:1620736625771&tbm=isch&source=iu&ictx=1&fir=AymqgxEoSzzyvM%252Ca7Wkb6mAFYRy3M%252C_&vet=1&usg=AI4_-kSdzLngLoiPj7KGMlqQYZ--2qEJ-g&sa=X&ved=2ahUKEwiL4Om20sHwAhWOY8AKHVcUDSUQ9QF6BAgVEAE#imgrc=AymqgxEoSzzyvM', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
