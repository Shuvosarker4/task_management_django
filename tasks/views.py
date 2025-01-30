from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from tasks.forms import TaskModelForm
from django.contrib import messages
# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request,"home.html",{"tasks":tasks})

def manager_dashboard(request):
    return render(request,"dashboard/manager_dashboard.html")

def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")

def create_task(request):
    form = TaskModelForm()
    if request.method == "POST":
        form =TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Task Created Successfully!!')
    return render(request,"CRUD/create_task.html",{"form":form})