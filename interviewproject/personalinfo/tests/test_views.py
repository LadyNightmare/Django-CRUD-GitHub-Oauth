from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..models import PersonalInfo

PERSONAL_INFO_DATA = {
        'name': 'name',
        'surname': 'surname',
        'address': 'current address',
        'title': 'Mrs.',
        'birth_date': '1999-02-02',
        'nationality': 'nationality',
        'phone_number': '657632381'
    }

class TestCreateInfoViews(TestCase):

    def setUp(self):
        self.client = Client()
        user = User(username="test", password="test")
        user.save()
        self.client.force_login(user=user)

    def test_create_info_GET_OK(self):
        response = self.client.get(reverse('create_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "personalinfo/personal_info_form.html")

    def test_create_info_POST(self):
        response = self.client.post(reverse('create_info'), PERSONAL_INFO_DATA, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "personalinfo/home.html")

    def test_create_info_POST_no_data(self):
        response = self.client.post(reverse('create_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "personalinfo/personal_info_form.html")

class TestUpdateDeleteInfo(TestCase):

    def setUp(self):
        self.client = Client()
        user = User(username="test", password="test")
        user.save()
        self.client.force_login(user=user)
        personal_info = PersonalInfo(user=user, name=  PERSONAL_INFO_DATA['name'], surname=  PERSONAL_INFO_DATA['surname'],
                                     current_address=  PERSONAL_INFO_DATA['address'],
                                     title=  PERSONAL_INFO_DATA['title'],
                                     birth_date=  PERSONAL_INFO_DATA['birth_date'], nationality=  PERSONAL_INFO_DATA['nationality'],
                                     phone_number=  PERSONAL_INFO_DATA['phone_number'])
        personal_info.save()

    def test_update_info_GET(self):
        response = self.client.get(reverse('update_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "personalinfo/personal_info_form.html")

    def test_update_info_POST(self):
        response = self.client.post(reverse('update_info'), PERSONAL_INFO_DATA, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "personalinfo/home.html")


    def test_update_info_POST_no_data(self):
        response = self.client.post(reverse('update_info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "personalinfo/personal_info_form.html")

    def test_logout(self):
        response = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "personalinfo/home.html")

    def test_delete_info(self):
        response = self.client.post(reverse('delete_info'))
        self.assertEqual(response.status_code, 302)
