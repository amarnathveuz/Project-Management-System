from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(task)
admin.site.register(company_master)
admin.site.register(User_details)
admin.site.register(user_active_account)
admin.site.register(Role_master)
admin.site.register(Role_mapping)
admin.site.register(user_permission_mapping)
admin.site.register(space_master)
admin.site.register(space_access_permission_user)