from ast import arg
from os import name, stat
from django import template
import json
register = template.Library()
from django.contrib.auth.models import User
from my_app.models import *
from datetime import date

@register.filter(name='company_nav_perm_check')
def company_nav_perm_check(value,args):
    print("value::",value)
    print("args::",args)
    user_dat = User.objects.get(id=value)
    try:
        user_details = User_details.objects.get(auth_user=user_dat)
    except:
        pass
    
    st = user_dat.is_superuser
    if st == True:
        if args == "Role" or args == "Team member":
            return False
        else:
            return True
    if user_details.user_type == "company_admin":
        if args == "Role" or args == "Team member":
            return True
    else:
        today = date.today()
        permission_status = False
        try:

            data_user_role = user_permission_mapping.objects.filter(auth_user_id=value,end_dt__gte=today,start_dt__lte=today) |  user_permission_mapping.objects.filter(auth_user_id=value,end_dt=None,start_dt__lte=today)
            role_id = list(data_user_role.values_list("role_mapping_id",flat=True))
            check_data = Role_mapping.objects.filter(role_master_id__in=role_id,navbar_name=args,read="True")
            if check_data:
                permission_status = True
            return permission_status
        except:
            return permission_status
        