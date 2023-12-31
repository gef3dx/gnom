# Generated by Django 4.1.7 on 2023-05-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0024_alter_product_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_order',
            field=models.DateField(blank=True, null=True, verbose_name='Дата заказа товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_shipment',
            field=models.DateField(blank=True, null=True, verbose_name='Дата поставки товара'),
        ),
    ]
