# Generated by Django 3.1.2 on 2021-08-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20210818_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
