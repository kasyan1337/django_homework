from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='Avatar',
                               help_text='Upload your avatar')
    phone = models.CharField(max_length=35, verbose_name='Phone number', blank=True, null=True,
                             help_text='Enter your phone number')
    country = models.CharField(max_length=35, verbose_name='Country', blank=True, null=True,
                               help_text='Enter your country')

    token = models.CharField(max_length=255, blank=True, null=True, verbose_name='token')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
