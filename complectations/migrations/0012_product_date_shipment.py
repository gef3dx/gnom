# Generated by Django 4.1.7 on 2023-05-20 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0011_alter_product_meas'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_shipment',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата поставки товара'),
            preserve_default=False,
        ),
    ]