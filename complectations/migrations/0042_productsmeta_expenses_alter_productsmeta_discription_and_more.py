# Generated by Django 4.1.7 on 2023-07-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0041_alter_product_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmeta',
            name='expenses',
            field=models.CharField(choices=[('Услуги', 'Услуги'), ('Закупки', 'Закупки')], default='Закупки', max_length=8, verbose_name='Вид ичесления'),
        ),
        migrations.AlterField(
            model_name='productsmeta',
            name='discription',
            field=models.TextField(blank=True, null=True, verbose_name='Описание товара или услуги'),
        ),
        migrations.AlterField(
            model_name='productsmeta',
            name='meas',
            field=models.CharField(choices=[('шт', 'штуки'), ('к/м', 'квадратные метры'), ('п/м', 'погоные метры'), ('литр', 'литры'), ('куб', 'кубы'), ('кг', 'килограмы')], default='1', max_length=8, verbose_name='Вид ичесления'),
        ),
    ]
