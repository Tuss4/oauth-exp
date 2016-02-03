from django.conf import settings
from django.core.urlresolvers import reverse
from .utils import get_scope_params, get_fields_params
from oauth.client import OauthClient
from oauth.utils import get_callback_url


FB_CLIENT = OauthClient(
    "{0}={1}&scope={2}&redirect_uri={3}".format(
        "https://www.facebook.com/dialog/oauth?client_id", settings.FACEBOOK_CLIENT_ID,
        get_scope_params(), get_callback_url('/fb/callback/')
    ),
    settings.FACEBOOK_EXCHANGE_URL
)
