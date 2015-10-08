from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):

    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        if self.first_name and self.last_name:
            return "{0} {1}".format(self.first_name, self.last_name)
        return self.email

    def __unicode__(self):
        return self.email
