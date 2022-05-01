from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee
from .test_utils import create_dummy_employee


class EmployeeTests(APITestCase):

    def test_create_employee(self):
        """
        Ensure that the create feature works
        """

        response = create_dummy_employee(self)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().first_name, 'Chuck')

    def test_full_update_employee(self):
        """
        Ensure that requests with PUT as method are working properly
        """
        create_dummy_employee(self)
        url = reverse('single-employee', kwargs={'pk': 1})
        data = {
            'first_name': 'Bob',
            'last_name': 'Norris',
            'department': 'sales',
            'birth_date': '1994-04-05'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.get().first_name, 'Bob')
        self.assertEqual(Employee.objects.get().department, 'sales')

    def test_partial_update_employee(self):
        """
        Ensure that requests with PATCH as method are working properly
        """
        create_dummy_employee(self)
        url = reverse('single-employee', kwargs={'pk': 1})
        data = {
            'birth_date': '1984-04-05'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # birth_date should have been updated
        self.assertEqual(Employee.objects.get().birth_date.strftime('%Y-%m-%d'), '1984-04-05')
        # other fields should stay unchanged
        self.assertEqual(Employee.objects.get().first_name, 'Chuck')
        self.assertEqual(Employee.objects.get().last_name, 'Norris')
        self.assertEqual(Employee.objects.get().department, 'personal')
