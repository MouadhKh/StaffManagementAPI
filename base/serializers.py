from rest_framework import serializers
from base.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'birth_date', 'department']

    # def run_validation(self, data):
    #     print(f"data_department:{data['department']}")
    #     ## Will most likely validate in the frontend in a real world scenario
    #     if data['department'].lower() not in ["personal", "sales", "development"]:
    #         raise serializers.ValidationError('Department not valid')
    #     return data.json()
