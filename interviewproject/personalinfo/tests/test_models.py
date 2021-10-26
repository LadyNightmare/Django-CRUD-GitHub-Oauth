from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import PersonalInfo


# Create your tests here.


class PersonalInfoTests(TestCase):
    LONG_STRING = " ".join(["This is a very long string with more than two hundred characters so it can be used "
                            "for all length constraints" for _ in range(3)])

    INCORRECT_FORMAT_STRING = 'inc0rrect_string'

    INCORRECT_LENGTH_TEST_CASES = [
        {
            'field': 'name',
            'name': LONG_STRING,
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'surname',
            'name': 'test name',
            'surname': LONG_STRING,
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'title',
            'name': 'test name',
            'surname': 'test surname',
            'title': LONG_STRING,
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'nationality',
            'name': 'test name',
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': LONG_STRING,
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'phone_number',
            'name': 'test name',
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+0346666666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'current_address',
            'name': 'test name',
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': LONG_STRING
        },
        {
            'field': 'past_address',
            'name': 'test name',
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': 'test current address',
            'past_address': LONG_STRING
        }
    ]

    INCORRECT_FORMAT_TEST_CASES = [
        {
            'field': 'name',
            'name': INCORRECT_FORMAT_STRING,
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'surname',
            'name': 'test name',
            'surname': INCORRECT_FORMAT_STRING,
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'birth_date',
            'name': 'test name',
            'surname': 'test_ surname',
            'title': 'Ms.',
            'birth_date': INCORRECT_FORMAT_STRING,
            'nationality': 'test nationality',
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'nationality',
            'name': 'test name',
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': INCORRECT_FORMAT_STRING,
            'phone_number': '+034666666666',
            'current_address': 'test current address'
        },
        {
            'field': 'phone_number',
            'name': 'test name',
            'surname': 'test surname',
            'title': 'Ms.',
            'birth_date': '1999-02-02',
            'nationality': 'test nationality',
            'phone_number': INCORRECT_FORMAT_STRING,
            'current_address': 'test current address'
        }
    ]

    def setUp(self):
        name = 'test name'
        current_address = 'test current address'
        past_address = 'test past address'
        surname = 'test surname'
        title = 'Ms.'
        birth_date = '1999-02-02'
        nationality = 'test nationality'
        phone_number = '+034666666666'
        self.user = User()
        self.user.save()
        self.correct_personal_info = PersonalInfo(user=self.user, name=name, surname=surname, current_address=current_address,
                                     title=title, past_address=past_address,
                                     birth_date=birth_date, nationality=nationality, phone_number=phone_number)

    def test_correct_fields_creation(self):
        self.correct_personal_info.full_clean()
        self.correct_personal_info.save()
        self.assertEqual(PersonalInfo.objects.filter(pk=self.correct_personal_info.pk).count(), 1)

    def test_incorrect_lengths(self):
        for test_case in self.INCORRECT_LENGTH_TEST_CASES:
            with self.subTest(msg=test_case['field']):
                personal_info = PersonalInfo(user=self.user, name=test_case['name'], surname=test_case['surname'],
                                             current_address=test_case['current_address'],
                                             title=test_case['title'],
                                             birth_date=test_case['birth_date'], nationality=test_case['nationality'],
                                             phone_number=test_case['phone_number'],
                                             past_address=test_case.get('past_address'))
                with self.assertRaises(ValidationError):
                    personal_info.full_clean()

    def test_incorrect_formats(self):
        for test_case in self.INCORRECT_FORMAT_TEST_CASES:
            with self.subTest(msg=test_case['field']):
                personal_info = PersonalInfo(user=self.user, name=test_case['name'], surname=test_case['surname'],
                                             current_address=test_case['current_address'],
                                             title=test_case['title'],
                                             birth_date=test_case['birth_date'], nationality=test_case['nationality'],
                                             phone_number=test_case['phone_number'],
                                             past_address=test_case.get('past_address'))
                with self.assertRaises(ValidationError):
                    personal_info.full_clean()

    def test_address_getter(self):
        self.correct_personal_info.full_clean()
        self.correct_personal_info.save()
        self.assertEqual(self.correct_personal_info.address, 'test current address')

    def test_address_setter(self):
        self.correct_personal_info.full_clean()
        self.correct_personal_info.save()
        old_address = self.correct_personal_info.current_address
        self.correct_personal_info.address = "new address"
        self.assertEqual(self.correct_personal_info.past_address, old_address)
        self.assertEqual(self.correct_personal_info.current_address, "new address")

    def test_personal_info_str(self):
        self.assertEqual(str(self.correct_personal_info), "Ms. test name test surname, test current address, "
                                                          "+034666666666, test nationality, 1999-02-02")