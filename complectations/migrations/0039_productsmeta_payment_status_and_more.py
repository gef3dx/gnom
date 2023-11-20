# Generated by Django 4.1.7 on 2023-07-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0038_groupproduct_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmeta',
            name='payment_status',
            field=models.CharField(choices=[('Оплатил', 'Оплатил'), ('Не оплатил', 'Не оплатил')], default='2', max_length=15, verbose_name='Статус оплаты'),
        ),
        migrations.AlterField(
            model_name='productsmeta',
            name='procent',
            field=models.IntegerField(default=35, verbose_name='Процент наценки %'),
        ),
    ]
