from django.contrib import admin
from django.urls import path
from Employeeapp  import views 

urlpatterns = [
    path('addleave/',views.LeaveCreateView.as_view(),name="leavecreate"),
    path('listleave/<int:id>/',views.ListempView.as_view(),name="listleave"),
    path('listleave/',views.ListempView.as_view(),name="listleave"),
]
