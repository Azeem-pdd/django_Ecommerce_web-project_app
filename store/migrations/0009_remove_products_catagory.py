# Generated by Django 3.1.2 on 2021-04-22 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210422_0956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='catagory',
        ),
    ]
