from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, fn=None, ln=None):
        user = self.model(email=email)
        user.first_name = fn
        user.last_name = ln
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, password=None, fn=None, ln=None):
        user = self.create_user(email, password, fn, ln)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user
