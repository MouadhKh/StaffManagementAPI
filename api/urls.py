from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view(), name='single-employee'),
]
