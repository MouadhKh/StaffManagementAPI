import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cgi_challenge.settings")
import django

django.setup()

from base.models import Employee
from enum import Enum
from faker import Faker
from faker_enum import EnumProvider
from model_bakery.recipe import Recipe

fake = Faker()
fake.add_provider(EnumProvider)


class Department(Enum):
    PERSONAL = "personal"
    SALES = "sales"
    DEVELOPMENT = "development"


for k in range(5):
    employee = Recipe(Employee,
                      first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=fake.date_of_birth(minimum_age=24, maximum_age=60),
                      department=fake.enum(Department).value
                      )
    employee.make()
