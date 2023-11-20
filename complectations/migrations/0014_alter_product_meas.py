# Generated by Django 4.1.7 on 2023-05-20 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0013_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='meas',
            field=models.CharField(choices=[('шт', 'штуки'), ('к/м', 'квадратные метры'), ('п/м', 'погоные метры'), ('литр', 'литры'), ('куб', 'кубы'), ('кг', 'килограмы')], default='1', max_length=8, verbose_name='Вид ичесления'),
        ),
    ]
