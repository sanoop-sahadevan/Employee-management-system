
from django.urls import path

from Adminapp import views

urlpatterns = [

    path('listemp/',views.EmployeeListApi.as_view(),name="emplist"),
    path('addemp/',views.EmployeeCreateApi.as_view(),name="addemp"),
    path('Editemp/<int:pk>/',views.EmployeeEditApi.as_view(),name="editemp"),
    path('deleteemp/<int:pk>/',views.EmployeeDeleteAPI.as_view(),name="delete"),

    # leavelist
    path('Listleave/',views.LeaveListempView.as_view(),name="listleave"),
    path('leaveupdate/<int:pk>/',views.Leaveupdate.as_view(),name="leaveupdate"),

    
    
]

