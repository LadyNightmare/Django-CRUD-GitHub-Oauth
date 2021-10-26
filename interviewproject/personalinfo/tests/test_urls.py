from django.test import TestCase
from django.urls import resolve, reverse

from ..views import create_info, update_info, delete_info, logout


class TestUrls(TestCase):

    def test_home_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).route, '')

    def test_create_info_resolves(self):
        url = reverse('create_info')
        self.assertEqual(resolve(url).func, create_info)

    def test_update_info_resolves(self):
        url = reverse('update_info')
        self.assertEqual(resolve(url).func, update_info)

    def test_delete_info_resolves(self):
        url = reverse('delete_info')
        self.assertEqual(resolve(url).func, delete_info)

    def test_login_ok_resolves(self):
        response = self.client.get(reverse('social:begin', kwargs={'backend': 'github'}))
        self.assertEqual(response.status_code, 302)

    def test_login_ko_resolves(self):
        url = reverse('social:begin', kwargs={'backend': 'facebook'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_logout_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)
