from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    meetings_attended = models.PositiveIntegerField(default=0)
    cohort = models.TextField(default='none')
    event = models.TextField(default='none')
    tshirt = models.TextField(default='none')
    grade = models.TextField(default='none')
    decaid = models.TextField(default='none')

    #undisplayed info
    cell_phone = models.TextField(default='none')
    parent_first_name = models.TextField(default='none')
    parent_last_name = models.TextField(default='none')
    parent_cell = models.TextField(default='none')
    parent_email = models.TextField(default='none')
    address = models.TextField(default='none')
    city = models.TextField(default='none')
    zipcode =  models.TextField(default='none')
    partners = models.TextField(default='none')
    bloodtype = models.TextField(default='none')
    physician = models.TextField(default='none')
    physicianPhone = models.TextField(default='noun')
    physicianAddress = models.TextField(default='none')
    insurance_number = models.TextField(default='none')
