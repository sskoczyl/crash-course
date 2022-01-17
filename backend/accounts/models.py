from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.utils.timezone import now
from datetime import timedelta

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
    value = models.CharField(
        primary_key=True, max_length=100, unique=True, blank=False, null=False
    )
    user = models.ForeignKey(
        CustomUser, blank=False, null=True, on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        default=now, unique=False, blank=False, null=False
    )

    objects = ActivationTokenManager()

    def __str__(self):
        return str(self.value)

    def get_token_value(self):
        return self.value

    def validate_token(self):
        """
        Returns TRUE if token is valid (was created less than 24h ago)
        """
        current_time = now()
        max_diffrence = timedelta(hours=24)

        return max_diffrence > current_time - self.date_created
