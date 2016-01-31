import requests
import json
from urllib.parse import urlunparse
from .exceptions import StatusNotOkay


class OauthClient(object):
    """
    Handles the OAuth 2.0 Handshake.
    Is initialized with the 3rd party client redirect url.
    """

    def __init__(self, redirect_url, exchange_url):
        self.redirect_url = redirect_url
        self.exchange_url = exchange_url
    # TODO: Raise a different type of exception instead of an assert.
    # Exchanges the code received
    # Building the URL based off the documentation for urlunparse convenience attributes in:
    # https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse

    def exchange(self, query, token_kwarg='access_token'):
        parts = ['https', self.exchange_url, '', '', query, '']
        url = urlunparse(parts)
        r = requests.get(url)
        if r.status_code != 200:
            raise StatusNotOkay(r.status_code)
        data = r.json()
        return data[token_kwarg]

    def get_profile(self, base_url, query):
        parts = ['https', base_url, '', '', query, '']
        url = urlunparse(parts)
        r = requests.get(url)
        if r.status_code != 200:
            raise StatusNotOkay(r.status_code)
        data = r.json()
        return data
