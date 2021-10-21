from django.db import models

TITLES = (
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.')
)

# Create your models here.
class PersonalInfo(models.Model):
    current_address = models.CharField(max_length=200, default='')
    past_address = models.CharField(max_length=200, blank=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    title = models.CharField(max_length=4, choices=TITLES, default='Ms.')
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    def __str__(self):
        return f"{self.title} {self.name} {self.surname}, {self.current_address}, {self.phone_number}, {self.nationality}, " \
               f"ZIP CODE: {self.birth_date}"
