from django.db import models
from users.models import CustomUser
from django.urls import reverse
from complectations.models.complectation import Complectation


# Модель поставщика
class Provider(models.Model):
    name = models.CharField(verbose_name="Имя поставщика", max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Поставщик сметы"
        verbose_name_plural = "Поставщики сметы"


# Модель прихода денег
class Receipts(models.Model):
    name = models.CharField(verbose_name="Название поступления", max_length=250)
    discription = models.TextField(verbose_name="Описание поступления", blank=True, null=True)
    date_create = models.DateField(verbose_name="Дата поступления")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма поступления", default=0)
    complectation = models.ForeignKey(Complectation, verbose_name="Выберите комплектацию", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, verbose_name="Добавил поступление", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('receiptsfromcomplet', args=[self.slug])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Поступление средств"
        verbose_name_plural = "Пуступления средств"


# Модель продукта закуки
class ProductSmeta(models.Model):

    PAYMENT_CHOICES = [
        ("Оплатил", "Оплатил"),
        ("Не оплатил", "Не оплатил"),
    ]

    name = models.CharField(verbose_name="Имя товара или услуги", max_length=50)
    discription = models.TextField(verbose_name="Описание товара или услуги", blank=True, null=True)
    date_create = models.DateField(verbose_name="Дата добавления чека")
    price = models.DecimalField(max_digits=12, decimal_places=2,verbose_name="Цена чека", default=0)
    provider = models.ForeignKey(Provider, verbose_name="Выберите поставщика", on_delete=models.PROTECT, blank=True, null=True)
    image = models.ImageField(verbose_name="Фото чека", upload_to="product/", blank=True)
    payment_status = models.CharField(verbose_name="Статус оплаты", max_length=15, choices=PAYMENT_CHOICES)
    author = models.ForeignKey(CustomUser, verbose_name="Автор", on_delete=models.CASCADE)
    complectation = models.ForeignKey(Complectation, verbose_name="Выберите комплектацию", on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('productfromcomplet', args=[self.slug])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Закупка"
        verbose_name_plural = "Закупки"


# Модель услуги
class ServiceSmeta(models.Model):

    PAYMENT_CHOICES = [
        ("Оплатил", "Оплатил"),
        ("Не оплатил", "Не оплатил"),
    ]
    
    MEAS_CHOICES = [
        ("шт", "штуки"),
        ("к/м", "квадратные метры"),
        ("п/м", "погоные метры"),
        ("литр", "литры"),
        ("куб", "кубы"),
        ("кг", "килограмы"),
    ]

    name = models.CharField(verbose_name="Имя услуги", max_length=50)
    discription = models.TextField(verbose_name="Описание услуги", blank=True, null=True)
    date_create = models.DateField(verbose_name="Дата добавления")
    meas = models.CharField(verbose_name="Вид ичесления", max_length=8, default="1", choices=MEAS_CHOICES)
    count = models.DecimalField(max_digits=12, decimal_places=1,verbose_name="Количество", default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2,verbose_name="Цена", default=0)
    price_all = models.DecimalField(max_digits=12, decimal_places=2,verbose_name="Цена за все", default=0)
    complectation = models.ForeignKey(Complectation, verbose_name="Выберите комплектацию", on_delete=models.CASCADE)
    procent = models.IntegerField(verbose_name="Процент %", default=0)
    price_procent = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сумма наценки", default=0)
    author = models.ForeignKey(CustomUser, verbose_name="Автор", on_delete=models.CASCADE)
    process_org = models.BooleanField(verbose_name="Организация процесса", default=False)
    payment_status = models.CharField(verbose_name="Статус оплаты", max_length=15, choices=PAYMENT_CHOICES)

    def get_absolute_url(self):
        return reverse('servicefromcomplet', args=[self.slug])

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    
    



