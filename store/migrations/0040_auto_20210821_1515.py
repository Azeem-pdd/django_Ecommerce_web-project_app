# Generated by Django 3.1.2 on 2021-08-21 10:15

from django.db import migrations, models
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_auto_20210821_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_name',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.fields.related.ManyToManyField, to='store.products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
