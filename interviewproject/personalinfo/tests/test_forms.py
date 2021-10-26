from django.test import TestCase

from ..forms import PersonalInfoForm


class TestForms(TestCase):
    VALID_FORM = {
        'name': 'name',
        'surname': 'surname',
        'address': 'current_address',
        'title': 'Mrs.',
        'birth_date': '1999-02-02',
        'nationality': 'nationality',
        'phone_number': '657632381'
    }

    def test_personal_info_form_valid_data(self):
        form = PersonalInfoForm(self.VALID_FORM)
        self.assertTrue(form.is_valid())

    def test_personal_info_form_empty_address(self):
        form = PersonalInfoForm(
            {
                'name': 'name',
                'surname': 'surname',
                'address': '',
                'title': 'Mrs.',
                'birth_date': '1999-02-02',
                'nationality': 'nationality',
                'phone_number': '657632381'
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertTrue('address' in form.errors.keys())
        self.assertEqual(form.errors['address'][0], 'This field is required.')

    def test_personal_info_form_no_data(self):
        form = PersonalInfoForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)
        # TODO comprobar errores

    def test_personal_info_form_address_is_set(self):
        # TODO
        pass
        # form = PersonalInfoForm(self.VALID_FORM)
        # self.assertTrue(form.is_valid())
        # personal_info = form.save()
        # self.assertEqual(personal_info.current_address, self.VALID_FORM['address'])
