from django.db import models
from users.models import CustomUser
from django.urls import reverse
from complectations.models.complectation import Complectation


class GroupProduct(models.Model):
    name = models.CharField(verbose_name="Имя группы", max_length=50)
    slug = models.SlugField(verbose_name="Ссылка на группу", max_length=20, unique=True, help_text="**Можно использовать толко латинские буквы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа коплектации"
        verbose_name_plural = "Группы коплектаций"


# Модель продукта
class Product(models.Model):

    MEAS_CHOICES = [
        ("шт", "штуки"),
        ("к/м", "квадратные метры"),
        ("п/м", "погоные метры"),
        ("литр", "литры"),
        ("куб", "кубы"),
        ("кг", "килограмы"),
    ]

    STATUS_CHOICES = [
        ("Не заказано", "Не заказано"),
        ("В пути", "В пути"),
        ("На складе", "На складе"),
    ]


    name = models.CharField(verbose_name="Имя товара", max_length=50)
    discription = models.TextField(verbose_name="Описание товара", null=True, blank=True)
    group = models.ForeignKey(GroupProduct, verbose_name="Группа продукта", on_delete=models.PROTECT, null=True, blank=True)
    count = models.DecimalField(max_digits=12, decimal_places=1, verbose_name="Количество товаров", default=0)
    meas = models.CharField(verbose_name="Вид ичесления", max_length=8, default="1", choices=MEAS_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена", default=0)
    prepayment = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Предоплата", default=0)
    remains = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Остаток",)
    date_create = models.DateField(verbose_name="Дата создания товара", auto_now=True)
    date_order = models.DateField(verbose_name="Дата заказа товара", null=True, blank=True) 
    date_shipment = models.DateField(verbose_name="Дата поставки товара" , null=True, blank=True)
    status = models.CharField(verbose_name="Статус товара", max_length=50, choices=STATUS_CHOICES, default="Не заказано")
    sklad = models.CharField(verbose_name="Склад", max_length=150, blank=True, default=" ")
    image = models.ImageField(verbose_name="Картинка товара", upload_to="product/", blank=True)
    complectation = models.ForeignKey(Complectation, verbose_name="Выберите комплектацию", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, verbose_name="Автор продукта", on_delete=models.CASCADE)
    sum_price_count = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена за все", )

    def get_absolute_url(self):
        return reverse('productfromcomplet', args=[self.slug])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"