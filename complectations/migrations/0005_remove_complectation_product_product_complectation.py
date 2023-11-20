# Generated by Django 4.1.7 on 2023-04-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0004_remove_product_complectation_productcound_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complectation',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='complectation',
            field=models.ManyToManyField(through='complectations.ProductCound', to='complectations.complectation', verbose_name='Выберите комплектацию'),
        ),
    ]