# Generated by Django 4.1.7 on 2023-04-28 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0006_alter_productcound_cound'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='count',
        ),
    ]