from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.http import HttpResponseRedirect
from django.conf import settings

from users.models import User
from oauth.utils import Client

import requests


CLIENT = Client(
    client_id=settings.FB_CLIENT_ID,
    client_secret=settings.FB_SECRET,
    redirect_uri=settings.FB_REDIRECT_URI,
    base_url='https://www.facebook.com/dialog/oauth',
    scope='public_profile'
)


class LoginView(views.APIView):

    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        r_url = CLIENT.get_authorize_url()
        return HttpResponseRedirect(r_url)


class FacebookCallBackView(views.APIView):

    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        code = request.query_params.get('code')
        if code:
            resp = CLIENT.exchange_token(code)
            a_token = resp.get('access_token')
            url = 'https://graph.facebook.com/me?access_token={0}'.format(a_token)
            r = requests.get(url)
            r_bod = r.json()
            print r_bod
            return Response(
                {"detail": "Welcome, {0}".format(r_bod['name'])},
                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)
