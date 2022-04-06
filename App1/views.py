from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App1.models import Task1


def testing(request):
    print("Hello")

    return render(request, "index.html")

def xyz(request):
    task = request.GET.get('task')
    taskddesc = request.GET.get('taskdesc')
    # cursor = connection.cursor()
    # query = "insert into App1_task1(task_name,task_details) values('"+task+ "','" +taskddesc+ "')"
    # cursor.execute(query)
    task1 = Task1(task_name=task, task_details=taskddesc)
    task1.save()
    query1 = "select * from App1_task1"
    cursor1 = connection.cursor()
    cursor1.execute(query1)
    data = cursor1.fetchall()
    data2 = Task1.objects.all()
    data1 = {"xyz": data2}
    return render(request, "new.html",data1)