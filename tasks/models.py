from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateField()

    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('IN_PROGRESS','In progress'),
        ('COMPLETED','Completed'),
    ]
    assigned_to = models.ManyToManyField(Employee,related_name='tasks')
    project = models.ForeignKey(Projects,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=100,choices=STATUS_CHOICES, default="PENDING")
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class TaskDetails(models.Model):
    HIGH = 'H'
    LOW ='L'
    MEDIUM ='M'
    PRIORITY_OPTIONS=[
        (HIGH,'High'),
        (LOW,'Low'),
        (MEDIUM,'Medium'),
    ]
    task = models.OneToOneField(Task,on_delete=models.DO_NOTHING,related_name='details')
    priority = models.CharField(max_length=1,choices=PRIORITY_OPTIONS,default='L')
    notes = models.TextField(blank=True,null=True)
    def __str__(self):
        return f"Details for task {self.task.title}"