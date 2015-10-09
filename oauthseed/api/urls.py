from django.conf.urls import url, patterns

import user_api


urlpatterns = patterns(
    '',
    url(r'^login/?$', user_api.LoginView.as_view(), name='login'),
    url(r'^fbcallback/?$', user_api.FacebookCallBackView.as_view(), name='fbcallback'),
    url(r'^twcallback/?$', user_api.TwitterCallBackView.as_view(), name='twcallback'),
)
