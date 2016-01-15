from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from string import ascii_lowercase

from datetime import date


class UserTest(APITestCase):

    def setUp(self):
        url = reverse('user-register')
        for l in ascii_lowercase[:10]:
            r = self.client.post(url, {
                'email': 'bro.{}@bruh.io'.format(l),
                'password': 'password1'
            })
            self.assertEqual(r.status_code, status.HTTP_201_CREATED)

        self.user = User.objects.get(email="bro.a@bruh.io")

    def test_create(self):
        url = reverse('user-register')
        r = self.client.post(url, {
            'email': 'bro0f4llbros@bruh.io',
            'password': 'password1'
        })
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(r.data['email'], 'bro0f4llbros@bruh.io')
        self.assertTrue(User.objects.filter(email='bro0f4llbros@bruh.io').exists())
        u = User.objects.get(email='bro0f4llbros@bruh.io')
        self.assertEqual(u.created.date(), date.today())
        self.assertFalse(u.first_name)
        self.assertFalse(u.last_name)
        self.assertEqual(u.get_full_name(), 'bro0f4llbros@bruh.io')
        self.assertEqual(u.get_short_name(), 'bro0f4llbros@bruh.io')
        self.assertTrue(u.is_active)
        self.assertFalse(u.is_admin)

    def test_login(self):
        url = reverse('user-login')
        r = self.client.post(url, {
            'email': 'bro.a@bruh.io',
            'password': 'password1'
        })
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        user = User.objects.get(email='bro.a@bruh.io')
        self.assertEqual(r.data['id'], user.pk)
        self.assertEqual(r.data['token'], user.auth_token.key)

    def test_list(self):
        url = reverse('user-list')
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user.auth_token.key)
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(r.data['count'], 10)

    def test_retrieve(self):
        pass
