from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):

    objects = UserManager()

    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    phone = models.CharField(verbose_name="Телефон", max_length=15, unique=True)
    is_client = models.BooleanField(verbose_name="Клиент", default=False, help_text="Отметьте, если пользователь \
                                                                                        является клиентом.")
    is_worker = models.BooleanField(verbose_name="Сотрудник", default=False, help_text="Отметьте, если пользователь \
                                                                                            является сотрудником.")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} - {self.email} - {self.last_name}"
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
