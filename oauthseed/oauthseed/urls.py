"""oauthseed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from usr.api import RegistrationViewSet, UserViewSet, LoginViewSet
from fbexample.api import FacebookLoginViewSet, FacebookCallbackViewSet

router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'v1/user', RegistrationViewSet, base_name='user')
router.register(r'v1/user', LoginViewSet, base_name='user')
router.register(r'v1/user', UserViewSet, base_name='user')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include('fbexample.urls'))
]

urlpatterns += router.urls
