from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def testing(request):
    print("Hello")
    request
    return render(request, "index.html")

def xyz(request):
    print("Hello")
    return HttpResponse("Hello this is xyz request")