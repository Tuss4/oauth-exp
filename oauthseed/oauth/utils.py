import urlparse
import urllib
import requests
import json

FACEBOOK_URL = 'https://graph.facebook.com/v2.3/oauth/access_token'


class Client(object):
    """
    The OAuth Client
    """
    def __init__(self, client_id=None, redirect_uri=None, base_url=None, **kwargs):
        self.client_id = client_id
        self.redirect_uri = redirect_uri
        self.base_url = base_url
        if 'client_secret' in kwargs:
            self.client_secret = kwargs['client_secret']
        if 'scope' in kwargs:
            self.scope = kwargs['scope']

    def build_url(self, url, **kwargs):
        parts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qs(parts[4]))
        query.update(kwargs)
        parts[4] = urllib.urlencode(query)
        return urlparse.urlunparse(parts)

    def get_authorize_url(self):
        return self.build_url(
            self.base_url, client_id=self.client_id, redirect_uri=self.redirect_uri,
            scope=self.scope)

    def exchange_token(self, code):
        url = self.build_url(
            FACEBOOK_URL,
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            client_secret=self.client_secret,
            code=code
        )
        r = requests.get(url)
        return r.json()

    def get_user_data(self, url, access_token):
        url = self.build_url(
            url,
            access_token=access_token
        )
        r = requests.get(url)
        return r.json()
