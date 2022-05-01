from django.urls import reverse


def create_dummy_employee(self):
    url = reverse('employee-list')
    data = {
        'first_name': 'Chuck',
        'last_name': 'Norris',
        'department': 'personal',
        'birth_date': '1994-04-05'
    }
    response = self.client.post(url, data, format='json')
    return response
