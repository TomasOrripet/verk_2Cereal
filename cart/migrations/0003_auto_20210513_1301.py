# Generated by Django 3.2 on 2021-05-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_usercart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercerealitem',
            name='cereal',
        ),
        migrations.RemoveField(
            model_name='ordercerealitem',
            name='order',
        ),
        migrations.AddField(
            model_name='usercart',
            name='quantity',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='orderCerealItem',
        ),
    ]