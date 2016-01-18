from fbexample.models import FBToken


class OauthBackend(object):

    """Used to authenticate the OAuth User."""

    def authenticate(self, fb_id=None, service=''):
        # Check the token and return a user.
        model = None
        if service == 'fb':
            model = FBToken
        print("MODEL:", model)
        if fb_id is not None:
            try:
                at = model.objects.get(facebook_id=db_id)
                print(at)
                return at.user
            except model.DoesNotExist:
                return None
        return None
