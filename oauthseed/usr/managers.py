from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token
from fbexample.models import FBToken


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        user = self.model(email=email.lower())
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

    def create_fb_user(self, email, fb_id, token, password=None, fname='', lname=''):
        user = self.create_user(email, password)
        user.first_name = fname
        user.last_name = lname
        user.save(using=self._db)
        FBToken.objects.create(user=user, facebook_id=fb_id, access_token=token)
        return user
