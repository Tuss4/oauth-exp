from django.conf.urls import url
from rest_framework import routers
from .api import FacebookLoginViewSet, FacebookCallbackViewSet

router = routers.SimpleRouter()
router.trailing_slash = '/?'
router.register(r'fb', FacebookLoginViewSet, base_name='fb')
router.register(r'fb', FacebookCallbackViewSet, base_name='fb')
urlpatterns = router.urls
