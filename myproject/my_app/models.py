from django.db import models
from django.contrib.auth.models import User

# Create your models here.


status_type = [
    ("To do","To do"),
    ("Completed","Completed"),
    ("Testing","Testing"),
     ("Onhold","Onhold"),

]

class task(models.Model):
    task_name = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=50,choices=status_type)


# Amritha Updates

class common_table(models.Model):
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_ownership",on_delete=models.CASCADE,null=True)
    created_dt = models.DateField(auto_now=True)
    updated_by =  models.ForeignKey(User, related_name="%(app_label)s_%(class)s_ownership1",on_delete=models.CASCADE,null=True)
    updated_dt = models.DateField(null=True)
    created_tm = models.TimeField(auto_now=True)
    updated_tm = models.TimeField(null=True)
    status = models.CharField(max_length=10, null=True)

    class Meta:
        abstract = True

class company_master(common_table):
    company_name = models.CharField(max_length=50,null=True)
    company_logo = models.FileField(upload_to="company_logo", null=True)
    tax_number = models.CharField(max_length=50, null=True)
    mobile = models.CharField(max_length=15, null=True)
    website = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)


password_generate_option = (
    ("Automatic","Automatic"),
    ("Manual","Manual"),
)

user_type = (
    ("company_admin","Company_admin"),
    ("company_user","Company_user")
)

class User_details(common_table):
    auth_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    company_id = models.ForeignKey(company_master, on_delete=models.CASCADE,related_name="user_details_company_id", null=True)
    company_name = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50,null=True)
    password_option =  models.CharField(max_length=50,choices=password_generate_option,null=True)
    password = models.CharField(max_length=50,null=True)
    user_type = models.CharField(max_length=20,choices=user_type,null=True)
    photo = models.FileField(upload_to="user_image", null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)


class Role_master(common_table):
    
    auth_user = models.ForeignKey(User,related_name="role_auth_id",on_delete=models.CASCADE,null=True)
    role_name = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)


navbar_name = (
    ("Company","Company"),
    ("User","User"),
    ("Role","Role"),
    ("Team member","Team member")
)

class Role_mapping(common_table):
    role_master_id = models.ForeignKey(Role_master,related_name="Role_master_role_id",on_delete=models.CASCADE,null=True)
    navbar_name = models.CharField(max_length=50,choices=navbar_name,null=True)
    read = models.BooleanField(null=True)
    write = models.BooleanField(null=True)
    edit = models.BooleanField(null=True)
    delete = models.BooleanField(null=True)
    view_all = models.BooleanField(null=True)
    manage_all = models.BooleanField(null=True)

class user_permission_mapping(common_table):
    auth_user_id = models.ForeignKey(User,related_name="user_permision_auth",on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User_details,related_name="user_permision_userid",on_delete=models.CASCADE,null=True)
    role_mapping_id = models.ForeignKey(Role_master,related_name="user_permission_role_id",on_delete=models.CASCADE,null=True)
    start_dt = models.DateField(null=True)
    end_dt = models.DateField(null=True)
    description = models.TextField(null=True)


class user_active_account(common_table):
    user_id = models.ForeignKey(User_details,related_name="login_user_active_userid",on_delete=models.CASCADE,null=True)
    active_user_id = models.ForeignKey(User_details,related_name="user_active_userid",on_delete=models.CASCADE,null=True)
    active_auth_user_id = models.ForeignKey(User,related_name="active_auth_id",on_delete=models.CASCADE,null=True)

class space_master(common_table):
    space_name = models.CharField(max_length=50,null=True)
    active_account_id = models.ForeignKey(User_details,related_name="space_active_userid",on_delete=models.CASCADE,null=True)
    added_user_id = models.ForeignKey(User,related_name="space_auth_id",on_delete=models.CASCADE,null=True)


class space_access_permission_user(common_table):
    space_id = models.ForeignKey(space_master,related_name="space_access_id",on_delete=models.CASCADE,null=True)
    invite_user_details_id = models.ForeignKey(User_details,related_name="space_access_userid",on_delete=models.CASCADE,null=True)
    invite_user_auth_id = models.ForeignKey(User,related_name="space_access_auth_id",on_delete=models.CASCADE,null=True)


class sub_space_master(common_table):
    space_id = models.ForeignKey(space_master,related_name="sub_space_master_id",on_delete=models.CASCADE,null=True)
    sub_space_name = models.CharField(max_length=50,null=True)
    active_account_id = models.ForeignKey(User_details,related_name="sup_space_master_userid",on_delete=models.CASCADE,null=True)
    added_user_id = models.ForeignKey(User,related_name="sub_space_master_auth_id",on_delete=models.CASCADE,null=True)


class sub_space_access_permission(common_table):
    space_id = models.ForeignKey(space_master,related_name="sub_space_access",on_delete=models.CASCADE,null=True)
    sub_space_id = models.ForeignKey(sub_space_master,related_name="sub_space_id",on_delete=models.CASCADE,null=True)
    invite_user_details_id = models.ForeignKey(User_details,related_name="sup_space_access_userid",on_delete=models.CASCADE,null=True)
    invite_user_auth_id = models.ForeignKey(User,related_name="sub_space_access_auth",on_delete=models.CASCADE,null=True)


buckets = (
    ("todo","To do"),
    ("completed","Completed"),
    ("testing","Testing"),
    ("onhold","On Hold")
)

progress = (
    ("not_started","Not Started"),
    ("inprogress","Inprogress"),
    ("completed","Completed"),
)
priority = (
    ("urgent","Urgent"),
    ("important","Important"),
    ("medium","Medium"),
    ("low","Low")
)

class Add_task_master(common_table):
    space_id = models.ForeignKey(space_master,related_name="add_task_space",on_delete=models.CASCADE,null=True)
    sub_space_id = models.ForeignKey(sub_space_master,related_name="add_sub_space",on_delete=models.CASCADE,null=True)
    task_name = models.CharField(max_length=50,null=True)
    buckets = models.CharField(max_length=50,choices=buckets,null=True)
    progress = models.CharField(max_length=50,choices=progress,null=True)
    priority = models.CharField(max_length=50,choices=priority,null=True)
    notes = models.TextField(null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

class Add_task_access_user(common_table):
    add_task = models.ForeignKey(Add_task_master,related_name="add_task_space",on_delete=models.CASCADE,null=True)
    invite_user_details_id = models.ForeignKey(User_details,related_name="add_task_user",on_delete=models.CASCADE,null=True)
    invite_user_auth_id = models.ForeignKey(User,related_name="add_task_auth",on_delete=models.CASCADE,null=True)

class Add_task_checklist(common_table):
    add_task_id = models.ForeignKey(Add_task_master,related_name="add_task_checklist",on_delete=models.CASCADE,null=True)
    item_name = models.CharField(max_length=50,null=True),


class Add_task_attachment(common_table):
    add_task_id = models.ForeignKey(Add_task_master,related_name="add_attachment",on_delete=models.CASCADE,null=True)
    file_name = models.CharField(max_length=50,null=True),
    file_type = models.CharField(max_length=30,null=True),
    attached_file = models.FileField(upload_to="task_attachment", null=True)   


class Add_task_comments(common_table):
    add_task_id = models.ForeignKey(Add_task_master,related_name="task_comments",on_delete=models.CASCADE,null=True)
    added_by = models.ForeignKey(User_details,related_name="task_comment_user",on_delete=models.CASCADE,null=True)
    user_auth_id = models.ForeignKey(User,related_name="task_comment_auth",on_delete=models.CASCADE,null=True)
    comments=  models.TextField(null=True)






    
    
