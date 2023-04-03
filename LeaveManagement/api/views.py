from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

# index page
class IndexView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # getting the current logined user
        user = request.user

        # cheecking for the logined user is super user or not 
        if user.is_superuser == 1:

            # content for super user
            content = {
                'PROJECT NAME':'EMPLOYEE MANAGMENT SYSTEM',
                '------------':'-------------------------',
                # 'ACCESS' :'**Please login  && Verify Your Token..!**',
                '------':'-------------------------',
                'LOGIN PAGE' : 'http://127.0.0.1:8000/api-auth/login/',
                'TOKEN GENERATION' : 'http://127.0.0.1:8000/api/token/',
                'TOKEN REFRESH' : 'http://127.0.0.1:8000/api/token/refresh/',
                # 'TOKEN VERIFICATION' : 'http://127.0.0.1:8000/api/token/verify/',
                ':::::::::::::::::::::::::':':::::::::::::::::::::::::',
                'CREATE EMPLOYEE' : 'http://127.0.0.1:8000/adminapp/addemp/',
                'EMPLOYEE LIST':'http://127.0.0.1:8000/adminapp/listemp/',
                'EMPLOYEE DETAILS' : 'http://127.0.0.1:8000/adminapp/Editemp/<int:pk>//',
                # '.......................':'...................................',
                'LEAVE APPLICATION LIST' : 'http://127.0.0.1:8000/adminapp/Listleave/',
                'LEAVE APPLICATION APPROVAL':'http://127.0.0.1:8000/adminapp/leaveupdate/<int:pk>/',
                # '.......................':'...................................',
                'LOGOUT' : 'http://127.0.0.1:8000/api-auth/logout/'
                
            }
            return Response(content)

        else:
            # content for non super user
            content = {
                'PROJECT NAME':'EMPLOYEE MANAGMENT SYSTEM',
                '------------':'-------------------------',
                'ACCESS' :'**Please login  && Verify Your Token..!**',
                '------':'-------------------------',
                'LOGIN PAGE' : 'http://127.0.0.1:8000/api-auth/login/',
                'TOKEN GENERATION' : 'http://127.0.0.1:8000/api/token/',
                'TOKEN REFRESH' : 'http://127.0.0.1:8000/api/token/refresh/',
                # 'TOKEN VERIFICATION' : 'http://127.0.0.1:8000/api/token/verify/',
                ':::::::::::::::::::::::::':':::::::::::::::::::::::::',
                'CREATE LEAVE APPLICATION' : 'http://127.0.0.1:8000/employapp/addleave/',
                'LEAVE APPLICATION LIST':'http://127.0.0.1:8000/employapp/listleave/<int:id>/',
                # 'LEAVE APPLICATION DETAILS' : 'http://127.0.0.1:8000/accounts/employee/leave-application/<id>/',
                '.......................':'...................................',
                'LOGOUT' : 'http://127.0.0.1:8000/api-auth/logout/'
                
            }
            return Response(content)