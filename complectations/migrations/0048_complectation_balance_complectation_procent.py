# Generated by Django 4.1.7 on 2023-07-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0047_servicesmeta_author_alter_productsmeta_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='complectation',
            name='balance',
            field=models.IntegerField(default=0, verbose_name='Баланс'),
        ),
        migrations.AddField(
            model_name='complectation',
            name='procent',
            field=models.IntegerField(default=0, verbose_name='Процент'),
        ),
    ]