# Generated by Django 4.1.7 on 2023-05-22 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0020_alter_product_date_order_alter_product_date_shipment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_order',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата заказа товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_shipment',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата поставки товара'),
        ),
    ]