from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.utils.timezone import now

import uuid

from .managers import CustomUserManager, ActivationTokenManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    display_name = models.CharField(max_length=30, blank=True, null=True, default=None)
    email = models.EmailField(_("email address"), unique=True, blank=False, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if self.display_name is not None:
            return self.display_name
        else:
            return str(self.email)


class ActivationToken(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user_id= models.ForeignKey(CustomUser, blank=False, null=True, on_delete=models.SET_NULL)
    date_created = models.DateField(default=now, unique=True, blank=False, null=False)

    objects = ActivationTokenManager()

    def get_token(self, user):

        token = uuid.uuid1()

        return token
