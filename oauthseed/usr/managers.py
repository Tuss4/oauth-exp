from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token
from fbexample.models import FBToken


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email.lower(), **kwargs)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
