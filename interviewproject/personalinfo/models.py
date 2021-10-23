from django.contrib.auth.models import User
from django.core.validators import RegexValidator
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
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    title = models.CharField(max_length=4, choices=TITLES, default='Ms.')
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
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
