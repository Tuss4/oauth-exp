from django.conf import settings


# Return callback url.
def get_callback_url(url):
    return ''.join([settings.CALLBACK_HOST, url])
