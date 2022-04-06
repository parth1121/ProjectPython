from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_details = models.CharField(max_length=1000)

class Task1(models.Model):
    task_name = models.CharField(max_length=100)
    task_details = models.CharField(max_length=1000)