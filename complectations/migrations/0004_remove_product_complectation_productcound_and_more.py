# Generated by Django 4.1.7 on 2023-04-28 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0003_remove_product_complectation_product_complectation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='complectation',
        ),
        migrations.CreateModel(
            name='ProductCound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cound', models.PositiveBigIntegerField(verbose_name='Количество')),
                ('complectation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complectations.complectation')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complectations.product')),
            ],
        ),
        migrations.AddField(
            model_name='complectation',
            name='product',
            field=models.ManyToManyField(through='complectations.ProductCound', to='complectations.product', verbose_name='Выберите комплектацию'),
        ),
    ]
