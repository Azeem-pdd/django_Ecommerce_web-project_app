# Generated by Django 3.1.2 on 2021-08-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_auto_20210818_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
