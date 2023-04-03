# from django.shortcuts import render
# from django.shortcuts import render
# from django.urls import reverse_lazy
# import requests
from requests import Response
from Employeeapp.models import Leave_employee
from .models import Employee,User
# from .serializers import Employee_listCreate_Serielizer
from .models import Employee
from .serializers import Employee_serializer,Leaveserializer,StatusSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters
# from rest_framework.authentication import SessionAuthentication,BasicAuthentication

from rest_framework  import generics

# Create your views here.


from rest_framework import generics, permissions
# Create your views here.







class EmployeeCreateApi(generics.CreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class =Employee_serializer

class EmployeeListApi(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = Employee.objects.all()
    serializer_class =Employee_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["employee_name"]
    ordering_fields = ["employee_name", "martial_status"]
   


class EmployeeEditApi(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class =Employee_serializer
 


class EmployeeDeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class =Employee_serializer
    # lookup_field = 'id'    








# listleaves of employee





class LeaveListempView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Leave_employee.objects.all()
    serializer_class =Leaveserializer

    # lookup_field='id'
    filter_backends = [filters.SearchFilter]
    search_fields = ["nature_of_leave"]
    ordering_fields = ["employee_name"]





 
class Leaveupdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    
    queryset = Leave_employee.objects.all()
    serializer_class =StatusSerializer
  



    


