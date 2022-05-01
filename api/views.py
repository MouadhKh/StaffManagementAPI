from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.views import get_swagger_view

from base.serializers import EmployeeSerializer
from base.models import Employee


class EmployeeList(APIView):
    def get(self, request):
        """
        List all employees

        <br>
        """
        employees = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return Response(employee_serializer.data)

    def post(self, request):
        """
        Create & Save an employee

        <i>-first_name:string,
        -last_name:string,
        -birth_date:yyyy-MM-dd
        -department:'personal','sales' or 'development'<i>
        """
        # Deserialize received data
        employee_serializer = EmployeeSerializer(data=request.data)
        employee_serializer.is_valid(raise_exception=True)
        employee_serializer.save()
        return Response(employee_serializer.data, status=status.HTTP_201_CREATED)


class EmployeeDetail(APIView):
    def get(self, request, pk):
        """
        Get single employee by id

        <br>
        """
        employee = get_object_or_404(Employee, id=pk)
        employee_serializer = EmployeeSerializer(employee)

        return Response(employee_serializer.data)

    def put(self, request, pk):
        """
        Update the whole employee(by id) (all fields)

        <br>
        """
        employee = get_object_or_404(Employee, id=pk)
        employee_serializer = EmployeeSerializer(employee, request.data)
        employee_serializer.is_valid(raise_exception=True)
        employee_serializer.save()
        return Response(employee_serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, pk):
        """
        Update particular field(s) in employee

        <br>
        """
        employee = get_object_or_404(Employee, id=pk)
        employee_serializer = EmployeeSerializer(employee, request.data, partial=True)
        employee_serializer.is_valid(raise_exception=True)
        employee_serializer.save()
        return Response(employee_serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        """
        Delete employee by  id

        <br>
        """
        employee = get_object_or_404(Employee, id=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
