from django.db import models
from complectations.models import Complectation
from users.models import CustomUser


class Tasks(models.Model):

    STATUS_CHOICES = [
        ("В ходе выполнения", "0"),
        ("Выполнил", "1"),
    ]

    title = models.CharField(verbose_name="Имя задачи", max_length=255)
    description = models.TextField(verbose_name="Описание задачи")
    complectation = models.ForeignKey(Complectation, verbose_name="Объект", on_delete=models.PROTECT)
    status = models.CharField(verbose_name="Статус задачи", max_length=50, choices=STATUS_CHOICES,
                              default="0")
    user = models.ManyToManyField(CustomUser, verbose_name="Выполняют задачу")
    date_create = models.DateField(verbose_name="Дата создания задачи", auto_now=True)
    date = models.DateField(verbose_name="Срок выполнения", null=True, blank=True)
    explanations = models.CharField(verbose_name="Пояснения", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"



