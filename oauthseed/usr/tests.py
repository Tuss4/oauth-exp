from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


class UserTest(APITestCase):

    def test_create_user(self):
        url = reverse('user-register')
        r = self.client.post(url, {
            'email': 'bro0f4llbros@bruh.io',
            'password': 'password1'
        })
        print(r.data)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
