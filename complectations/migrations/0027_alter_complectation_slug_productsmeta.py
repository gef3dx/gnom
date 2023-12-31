# Generated by Django 4.1.7 on 2023-07-03 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('complectations', '0026_remove_complectation_author_complectation_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complectation',
            name='slug',
            field=models.SlugField(help_text='**Можно использовать толко латинские буквы', max_length=20, unique=True, verbose_name='Ссылка на комплектацию'),
        ),
        migrations.CreateModel(
            name='ProductSmeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя товара')),
                ('discription', models.TextField(verbose_name='Описание товара')),
                ('count', models.IntegerField(default=0, verbose_name='Количество товара')),
                ('meas', models.CharField(choices=[('шт', 'штуки'), ('к/м', 'квадратные метры'), ('п/м', 'погоные метры'), ('литр', 'литры'), ('куб', 'кубы'), ('кг', 'килограмы')], default='1', max_length=8, verbose_name='Вид ичесления')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('prepayment', models.IntegerField(default=0, verbose_name='Предоплата')),
                ('remains', models.IntegerField(verbose_name='Остаток')),
                ('date_create', models.DateField(auto_now=True, verbose_name='Дата создания товара')),
                ('image', models.ImageField(blank=True, upload_to='product/', verbose_name='Фото чека')),
                ('sum_price_count', models.IntegerField(verbose_name='Цена за все')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор продукта')),
                ('complectation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complectations.complectation', verbose_name='Выберите комплектацию')),
            ],
            options={
                'verbose_name': 'Продукт сметы',
                'verbose_name_plural': 'Продукты сметы',
            },
        ),
    ]
