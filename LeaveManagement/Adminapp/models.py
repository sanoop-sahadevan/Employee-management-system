# from django.contrib.auth.models import AbstractBaseUser
# from django.db import models
# from django.contrib.auth.models import User

# # class User(AbstractBaseUser):
# #     email = models.EmailField(max_length=255, unique=True)
# #     is_admin = models.BooleanField(default=False)
# #     is_employee = models.BooleanField(default=False)

# #     USERNAME_FIELD = 'email'

# #     class Meta:
# #         abstract = True

# class Employee(models.Model):
#     # employee=models.ForeignKey(User,on_delete=models.CASCADE)
#     pswd=models.CharField(max_length=100)
#     email_id=models.EmailField(unique=True)
#     employee_name = models.CharField(max_length=255)
#     contact_number = models.CharField(max_length=255)
#     emergency_contact_number = models.CharField(max_length=255)
#     address = models.TextField()
#     position = models.CharField(max_length=255)
#     dob = models.DateField()
#     martial_status = models.CharField(max_length=255)
#     blood_group = models.CharField(max_length=255)
#     job_title = models.CharField(max_length=255)
#     work_location = models.CharField(max_length=255)
#     # date_of_joining = models.DateField()
#     reporting_to = models.CharField(max_length=255)
#     linkedin_link = models.URLField(max_length=255)

#     # is_employee = True

# # class Admin(
    





from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=50,null=False)
    contact_number =models.IntegerField()
    emergency_contact_number = models.IntegerField()
    address = models.TextField()
    postion = models.CharField(max_length=250)
    dob = models.DateField()
    martial_status = models.BooleanField(default=False)
    blood_group = models.CharField(max_length=10)
    job_title = models.CharField(max_length=250)
    work_location = models.CharField(max_length=250)
    date_of_joining = models.DateField(auto_now=True)
    reporting_to = models.CharField(max_length=250)
    linked_in = models.URLField(max_length=250)
    profile_picture = models.ImageField(upload_to='media/profile', blank=True)
    email = models.EmailField(unique=True,null=False)
    password = models.CharField(max_length=100)
  
    
    def __str__(self):
        return self.employee_name