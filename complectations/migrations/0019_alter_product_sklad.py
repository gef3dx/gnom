# Generated by Django 4.1.7 on 2023-05-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0018_product_sklad_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sklad',
            field=models.CharField(default=' ', max_length=150, verbose_name='Склад'),
        ),
    ]
