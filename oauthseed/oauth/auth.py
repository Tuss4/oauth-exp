from fbexample.models import FBToken


class OauthBackend(object):

    """Used to authenticate the OAuth User."""

    def authenticate(self, token=None, service=''):
        # Check the token and return a user.
        model = None
        if service == 'fb':
            model = FBToken
        print("MODEL:", model)
        if token is not None:
            print(token)
            try:
                at = model.objects.get(access_token=token)
                print(at)
                return at.user
            except model.DoesNotExist:
                return None
        return None
