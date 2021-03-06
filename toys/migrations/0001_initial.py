# Generated by Django 3.2 on 2021-05-12 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cereal', '0005_alter_cereal_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='toys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toyName', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=999, null=True)),
                ('price', models.FloatField()),
                ('amountInStock', models.FloatField()),
                ('type', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=99999, null=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cereal.manufacturer')),
            ],
        ),
    ]
