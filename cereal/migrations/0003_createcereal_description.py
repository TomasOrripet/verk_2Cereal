# Generated by Django 3.2 on 2021-05-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0002_auto_20210510_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='createcereal',
            name='description',
            field=models.CharField(max_length=999, null=True),
        ),
    ]
