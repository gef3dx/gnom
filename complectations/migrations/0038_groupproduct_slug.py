# Generated by Django 4.1.7 on 2023-07-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complectations', '0037_product_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupproduct',
            name='slug',
            field=models.SlugField(default='/', help_text='**Можно использовать толко латинские буквы', max_length=20, unique=True, verbose_name='Ссылка на группу'),
            preserve_default=False,
        ),
    ]
