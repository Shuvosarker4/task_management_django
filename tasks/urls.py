from django.urls import path
from tasks.views import home,manager_dashboard,user_dashboard

urlpatterns = [
    path('home/', home),
    path('manager-dashboard/', manager_dashboard,name="manager-dashboard"),
    path('user-dashboard/', user_dashboard,name="user-dashboard"),
]
