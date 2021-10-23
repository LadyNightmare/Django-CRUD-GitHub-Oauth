from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxValueValidator
from datetime import date
from django.db import models

TITLES = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.')
)


# Create your models here.
class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_address = models.CharField(max_length=200)
    past_address = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=50,
                            validators=[
                                RegexValidator(
                                    regex='^[a-zA-ZÀ-ÿ\u00f1\u00d1]*(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',
                                    message='Only letters allowed.'
                                )
                            ]
                            )
    surname = models.CharField(max_length=50,
                               validators=[
                                   RegexValidator(
                                       regex='^[a-zA-ZÀ-ÿ\u00f1\u00d1]*(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',
                                       message='Only letters allowed.'
                                   )
                               ]
                               )
    title = models.CharField(max_length=4, choices=TITLES, default='Ms.')
    birth_date = models.DateField(validators=[MaxValueValidator(limit_value=date.today)])
    nationality = models.CharField(max_length=50,
                                   validators=[
                                       RegexValidator(
                                           regex='^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$',
                                           message='Only letters allowed.'
                                       )
                                   ]
                                   )
    phone_number = models.CharField(max_length=20,
                                    validators=[
                                        RegexValidator(
                                            regex='^[0-9\-\+]{9,15}$',
                                            message='Phone format is invalid! Valid formats are +12 123456789, +1234 123456789, +12123456789 and +1234123456789'
                                        )
                                    ]
                                    )

    def __str__(self):
        return f"{self.title} {self.name} {self.surname}, {self.current_address}, {self.phone_number}, {self.nationality}, " \
               f"{self.birth_date}"

    @property
    def address(self):
        return self.current_address

    @address.setter
    def address(self, value):
        if value != self.current_address:
            self.past_address = self.current_address
            self.current_address = value
