from django.urls import path
from tasks.views import home,manager_dashboard,user_dashboard,create_task,update_task,delete_task

urlpatterns = [
    path('home/', home),
    path('manager-dashboard/', manager_dashboard,name="manager-dashboard"),
    path('user-dashboard/', user_dashboard,name="user-dashboard"),
    path('create_task/', create_task,name="create-task"),
    path('update_task/<int:id>/', update_task,name="update-task"),
    path('delete_task/<int:id>/', delete_task,name="delete-task"),
]
