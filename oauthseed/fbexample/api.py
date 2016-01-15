from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import get_user_model
from oauth.client import OauthClient
from oauth.auth import OauthBackend
import requests
from collections import OrderedDict
from .models import FBToken


FB_CLIENT = OauthClient(
    "{0}={1}&scope={2}&redirect_uri={3}".format(
        "https://www.facebook.com/dialog/oauth?client_id", settings.FACEBOOK_CLIENT_ID,
        "email", "https://f61b37ef.ngrok.io/v1/fb/callback/"
    ),
    "graph.facebook.com/v2.5/oauth/access_token"
)


class FacebookLoginViewSet(viewsets.GenericViewSet):

    @list_route(methods=['GET'], permission_classes=[AllowAny])
    def login(self, request):
        return HttpResponseRedirect(FB_CLIENT.redirect_url)


class FacebookCallbackViewSet(viewsets.GenericViewSet):

    @list_route(methods=['GET'], permission_classes=[AllowAny])
    def callback(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if not code:
            return Response(
                {'detail': 'You did not authorize us.'}, status=status.HTTP_401_UNAUTHORIZED)
        query = "client_id={0}&redirect_uri={1}&client_secret={2}&code={3}".format(
            settings.FACEBOOK_CLIENT_ID, FB_CLIENT.redirect_url,
            settings.FACEBOOK_CLIENT_SECRET, code
        )
        at = FB_CLIENT.exchange(query)

        profile = FB_CLIENT.get_profile(
            "graph.facebook.com/v2.5/me",
            "fields=email,first_name,last_name&access_token={}".format(at))
        try:
            fb = FBToken.objects.get(facebook_id=profile['id'])
            r = OrderedDict()
            r['id'] = fb.user.pk
            r['token'] = fb.user.auth_token.key
            return Response(r, status=status.HTTP_200_OK)
        except FBToken.DoesNotExist:
            u = get_user_model().objects.create_fb_user(
                email=profile['email'], fb_id=profile['id'], token=at,
                fname=profile['first_name'], lname=profile['last_name'])
            r = OrderedDict()
            r['id'] = u.pk
            r['token'] = u.auth_token.key
            return Response(r, status=status.HTTP_200_OK)
