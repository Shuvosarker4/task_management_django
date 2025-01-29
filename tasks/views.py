from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to event management project")

def manager_dashboard(request):
    return render(request,"dashboard/manager_dashboard.html")

def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")