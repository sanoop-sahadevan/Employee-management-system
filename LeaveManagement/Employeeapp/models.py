


from django.db import models
# from Adminapp.models import Employee
from django.contrib.auth.models import User


class Leave_employee(models.Model):
    NATURE_OF_LEAVE_CHOICES = (
        ('Sick', 'Sick'),
        ('Vacation', 'Vacation'),
    ),
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    )


    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    apply_date = models.DateField(auto_now=False, auto_now_add=True, editable=False)
    nature_of_leave = models.CharField(max_length=250,choices=( ('Sick', 'Sick'),
        ('Vacation', 'Vacation')))
    first_day = models.DateField()
    last_day = models.DateField()
    number_of_days = models.IntegerField()
    status = models.CharField(max_length=20, default='pending',
                              choices=( ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected')))

  
    def __str__(self):
        return self.employee        

