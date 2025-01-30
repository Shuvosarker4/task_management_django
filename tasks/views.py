from django.shortcuts import render,redirect
from tasks.models import Task
from tasks.forms import TaskModelForm,TaskDetailModelForm
from django.contrib import messages
from django.db.models import Q,Count
from datetime import date
# Create your views here.
def home(request):
    # tasks = Project.objects.all()
    # tasks = Task.objects.select_related('project').all()
    # first_task = Task.objects.first()
    return render(request,"home.html")

def manager_dashboard(request):
    type = request.GET.get('type','all')
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
    if type == 'completed':
        tasks=base_query.filter(status="COMPLETED")
    elif type == 'pending':
        tasks=base_query.filter(status="PENDING")
    elif type == 'in-progress':
        tasks=base_query.filter(status="IN_PROGRESS")
    elif type == 'all':
        tasks=base_query.all()

    count = Task.objects.aggregate(
        total_task =Count('id'),
        pending_task = Count('id',filter=Q(status="PENDING")),
        in_progress_task = Count('id',filter=Q(status="IN_PROGRESS")),
        completed_task = Count('id',filter=Q(status="COMPLETED")),
    )

    context={
        "tasks":tasks,
        'counts':count
    }
    return render(request,"dashboard/manager_dashboard.html",context)

def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")

def create_task(request):
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()
    if request.method == "POST":
        task_form =TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_details = task_detail_form.save(commit=False)
            task_details.task = task
            task_details.save()
            messages.success(request,'Task Created Successfully!!')
            return redirect('create-task')
    return render(request,"CRUD/create_task.html",{"form":task_form,"task_details_form":task_detail_form})

def update_task(request,id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)
    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)
    if request.method == "POST":
        task_form =TaskModelForm(request.POST,instance=task)
        task_detail_form = TaskDetailModelForm(request.POST,instance=task.details)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_details = task_detail_form.save(commit=False)
            task_details.task = task
            task_details.save()
            messages.success(request,'Task Updated Successfully!!')
            return redirect('update-task',id)
    
    return render(request,'CRUD/create_task.html',{"form":task_form,"task_details_form":task_detail_form})

def delete_task(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request,'Task deleted successfully!')
        return redirect('manager-dashboard')
    else:
        messages.error(request,'Something went wrong!')
        return redirect('manager-dashboard')