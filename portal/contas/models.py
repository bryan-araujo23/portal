from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,password=password,**extra_fields)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractUser): 
    TYPE_USER = [
                ('ad', 'Administrador'), 
                ('co', 'Colaborador'),
                ('us', 'Usúario Padrão')
            ]    
    type_user = models.CharField('type user', max_length=2, choices=TYPE_USER, default='us')
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,) 
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_staff =  models.BooleanField('User Staff', default=True)
    is_active = models.BooleanField('User Active',default=False)
    is_admin = models.BooleanField('User Admin', default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'type_user', 'is_active']

    class Meta:
        verbose_name = 'Usúario'
        verbose_name_plural = 'Usúarios'
        ordering = ['first_name']

    def __str__(self):
        return self.email 
   