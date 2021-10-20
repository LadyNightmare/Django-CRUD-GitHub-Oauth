from django.contrib import admin
from django.db import models
from .models import Address, PersonalInfo

# Register your models here.

admin.site.register(PersonalInfo)