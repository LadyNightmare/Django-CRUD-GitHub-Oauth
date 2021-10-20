from django.db import models

TITLES = (
    ('Mr.','Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.','Ms.')
)

# Create your models here.
class Address(models.Model):
    street_line_one = models.CharField(max_length=100)
    street_line_two = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

class PersonalInfo(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    title = models.CharField(max_length=4, choices=TITLES, default='Ms.')
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=0)