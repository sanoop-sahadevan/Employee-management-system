from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User
from Employeeapp.models import Leave_employee


# - Show: Employee id, Employee Name, contact, Email, Designation, Reporting to, Work location.
class Employee_serializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        # fields=('__all__')
        exclude = ['employee']


    def create(self, validated_data):

        # validating the data
        employee = User(email=self.validated_data['email'], username=self.validated_data['email'])
        password =  self.validated_data['password']
        
        # password converting into hashed format
        employee.set_password(password)
        
        # employee email and username and password is saving in User table
        employee.save()
        
        # creating the new employee and stores in Employee table
        return Employee.objects.create(**validated_data,employee=employee)


class Leaveserializer(serializers.ModelSerializer):
    # employee_name=serializers.SerializerMethodField()
    # STATUS_CHOICES=()
    class Meta:
        model= Leave_employee
        fields=["apply_date","nature_of_leave","last_day" , "number_of_days","status","employee"]

     

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Leave_employee
        fields=['status']

       