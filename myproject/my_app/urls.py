from django.contrib import admin
from django import views
from django.urls import path,include

from . import views

urlpatterns = [
    path('sample',views.sample,name='sample'),
    path('task_status_update_api',views.task_status_update_api,name='task_status_update_api'),

    # Amritha Updates
    path('',views.login_page,name=''),
    path('index',views.index,name='index'),
    path('login_action',views.login_action,name='login_action'),
    path('base',views.base,name='base'),

    path('company_management',views.company_management,name='company_management'),
    path('comapny_add_action',views.comapny_add_action,name='comapny_add_action'),
    path('company_edit_modal_function',views.company_edit_modal_function,name='company_edit_modal_function'),
    path('company_update_action',views.company_update_action,name='company_update_action'),

    path('user_management',views.user_management,name='user_management'),
    
    path('user_add_action',views.user_add_action,name='user_add_action'),
    path('user_edit_modal_function',views.user_edit_modal_function,name='user_edit_modal_function'),
    path('user_update_action',views.user_update_action,name='user_update_action'),

    path('member_management',views.member_management,name='member_management'),

    path('space_add_action',views.space_add_action,name='space_add_action'),

    path('user_management_action',views.user_management_action,name='user_management_action'),


    path('role_management',views.role_management,name='role_management'),
    path('role_management_action',views.role_management_action,name='role_management_action'),





    
    
]
