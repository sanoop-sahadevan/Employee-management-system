from rest_framework import filters
from rest_framework import generics
# from rest_framework.views import 
from rest_framework.views import APIView

from rest_framework.response import Response
from .serializers import EmployeeLeaveCreateSeriliazer, Leavelist
from .models import Leave_employee


from rest_framework import generics, permissions, authentication


#

# Create your views here.


class LeaveCreateView(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = Leave_employee.objects.all()

    serializer_class = EmployeeLeaveCreateSeriliazer

    def create(self, request, *args, **kwargs):

        employee = request.user
        print(employee.id)

        if employee.is_superuser == 0:

            serializer = EmployeeLeaveCreateSeriliazer(
                data=request.data, context={'employee': employee})
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)

        else:

            return Response({'message': 'Only Employee can access this Page'})


class ListempView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["nature_of_leave"]
    ordering_fields = ["employee_name"]
    

    def get(self, request, format=None):
        employee = request.user
        queryset = Leave_employee.objects.filter(employee_id=employee.id)
        serializer_class =Leavelist(queryset, many=True)
        return Response(data=serializer_class.data)
    


    