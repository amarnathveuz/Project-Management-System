from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.index,name=''),
    path('task_status_update_api',views.task_status_update_api,name='task_status_update_api'),
    

    
]
