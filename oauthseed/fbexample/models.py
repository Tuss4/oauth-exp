from django.db import models
from django.conf import settings


class FBToken(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='fb_tokens')
    access_token = models.CharField(max_length=400)
    facebook_id = models.CharField(max_length=100)
