from django.contrib import admin
from django.urls import path

from App1.views import testing, xyz, edittask

urlpatterns = [
    path('test', testing),
    path('xyz', xyz),
    path('edittask/', edittask)
]