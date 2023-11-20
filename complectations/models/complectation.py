from django.db import models
from users.models import CustomUser

# Модель комплектации
class Complectation(models.Model):
    name = models.CharField(verbose_name="Имя Комплектации", max_length=50)
    adress = models.CharField(verbose_name="Адрес заказчика", max_length=150)
    phone = models.CharField(verbose_name="Телефон заказчика", max_length=15)
    slug = models.SlugField(verbose_name="Ссылка на комплектацию", max_length=20, unique=True, help_text="**Можно использовать толко латинские буквы")
    date_create = models.DateField(verbose_name="Дата создания коплектации", auto_now=True)
    users = models.ManyToManyField(CustomUser, verbose_name="Доступ пользователей к комплектации")
    balance = models.IntegerField(verbose_name="Баланс", default=0)
    procent = models.IntegerField(verbose_name="Процент", default=0)
   

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Комплектация"
        verbose_name_plural = "Комплектации"