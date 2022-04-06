from django.contrib import admin

# Register your models here.
from App1.models import  Employee, Task

admin.site.register(Employee)
admin.site.register(Task)