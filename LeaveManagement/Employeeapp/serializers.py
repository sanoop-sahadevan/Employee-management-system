from rest_framework import serializers

# from Adminapp.serializers import Employee_serializer
from .models import Leave_employee


class EmployeeLeaveCreateSeriliazer(serializers.ModelSerializer):
    # employee_name=serializers.StringRelatedField()y
    class Meta:
        model = Leave_employee

        exclude = ['employee', 'status']

    def create(self, validated_data):

        employee = self.context.get('employee')

        return Leave_employee.objects.create(**validated_data, employee=employee)


class Leavelist(serializers.ModelSerializer):
    class Meta:
        model = Leave_employee
        exclude = ["id", "employee"]

    def get(self, request, format=None):
        employee = request.user
        return Leave_employee.objects.filter(employee_id=employee.id)
