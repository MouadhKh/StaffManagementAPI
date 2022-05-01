from django.db import models
from birthday import BirthdayField, BirthdayManager

PERSONAL = 'personal'
SALES = 'sales'
DEVELOPMENT = 'development'


class Employee(models.Model):
    DEPARTMENT_CHOICES = (
        (PERSONAL, PERSONAL),
        (SALES, SALES),
        (DEVELOPMENT, DEVELOPMENT)
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = BirthdayField()
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)
