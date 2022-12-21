from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from rest_framework.decorators import api_view


# Create your views here.

from .models import task

def sample(request):
    todo_model_data  = task.objects.filter(status="To do")
    completed_model_data  = task.objects.filter(status="Completed")
    Testing_model_data  = task.objects.filter(status="Testing")
    Onhold_model_data  = task.objects.filter(status="Onhold")
    context = {
        'todo_mdoel_data':todo_model_data,
        'completed_mdoel_data':completed_model_data,
        'Testing_mdoel_data':Testing_model_data,
        'Onhold_mdoel_data':Onhold_model_data


    }
    return render(request,'sample.html',context)

from django.http import JsonResponse
def task_status_update_api(request):
    status = request.GET.get("status")
    id = request.GET.get("vid")
    print("status::::",str(status))
    print("id::::",str(id))
    update_data = task.objects.filter(id=id).update(status=status)
    return JsonResponse({"message":"success"})


# Amritha updates    

def index(request):
    user_data = User.objects.all().first()
    member_data = User_details.objects.all().exclude(created_by = user_data)
    space_master_data = ""
    try:
        userdetails_data = User_details.objects.get(auth_user=request.user)

        # if user is company_admin (navab sir (all space of him))
        if userdetails_data.user_type == "company_admin":
            space_master_data = space_master.objects.filter(added_user_id=request.user)
    
        else:
            # if user is company_user(their space only)
            space_access_data = space_access_permission_user.objects.get(invite_user_auth_id=request.user)
            space_master_data = space_master.objects.filter(id=space_access_data.space_id.id)
    except:
        pass

    context = {
        "member_data" : member_data,
        "space_master_data":space_master_data
    }
    return render(request, 'index.html',context)


def login_page(request):
    return render(request,'login.html')

def base(request):
    return render(request, 'base.html')




from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login


def login_action(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            user_data = ""
            try:
                user_data = User_details.objects.get(auth_user=user)
                print("user_data", user_data)
            except:
                pass
        
            st = user.is_superuser
            if user is not None:
                if st == True:
                    login(request, user)
                    return redirect('index')
                elif user_data:
                    login(request, user)
                    return redirect('index')
        except:
            messages.error(request, str("Incorrect username or password"))
            return redirect(request.META['HTTP_REFERER'])

                

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# @api_view(['GET'])
# def company_management(request,*args,**kwargs):
#     models_data = company_master.objects.all().order_by('?')[0]   
#     return Response(models_data,template_name = 'company_management.html')

# -----------------------------------------------------company_management-----------------------------------------------------------------

def company_management(request):

    user_data = User.objects.all().first()
    member_data = User_details.objects.all().exclude(created_by = user_data)
   
    data = company_master.objects.all()
    context = {
        "data" : data,
        "member_data" : member_data
    }
    
    return render(request, 'company_management.html',context)
    
from PIL import Image
import os
import PIL
import glob
import cv2
def comapny_add_action(request):
    if request.method == "POST":
        companyname = request.POST.get("companyname",False)
        logo =  request.FILES['logo']

        fixed_height = 400
        image = Image.open(logo)
        print("image.size",image.size)
        width_size = int(fixed_height/image.height * image.width)
        print("width_size:::::",width_size)
        resized_image = image.resize((width_size,fixed_height))
        print("resizeeeeeed:",resized_image.size)
        from django.conf import settings
        resized_image.save("media/company_logo/"+logo.name,quality=100)
        image_new1 = 'company_logo/'+logo.name
        
        tax_no = request.POST.get("tax_no",False)
        mobile_no = request.POST.get("mobile_no",False)
        website = request.POST.get("website",False)
        phone = request.POST.get("phone",False)
        email = request.POST.get("email",False)
        address = request.POST.get("address",False)

        if company_master.objects.filter(company_name=companyname).exists():
            messages.error(request,"Company name already exists")
            return redirect(request.META['HTTP_REFERER'])
        else:
            company_master.objects.create(
                company_name =companyname,
                company_logo = image_new1,
                tax_number = tax_no,
                mobile = mobile_no,
                website = website,
                phone = phone,
                email = email,
                address = address,
                created_by = request.user,
                status = "True"
                )
            messages.success(request,"Successfully added company details")
            return redirect(request.META['HTTP_REFERER'])


def company_edit_modal_function(request):
    id = request.GET.get("id",False)
    print("idddddddd",id)
    data = company_master.objects.get(id=id)
    
    context = {
        "data" : data,
    }
    return render(request,'company_edit_modal_function.html',context)
from datetime import datetime
from datetime import date
def company_update_action(request):
     if request.method == "POST":
        id = request.POST.get("id",False)
        companyname = request.POST.get("companyname",False)
        logo =  request.FILES['logo']

        fixed_height = 400
        image = Image.open(logo)
        print("image.size",image.size)
        width_size = int(fixed_height/image.height * image.width)
        resized_image = image.resize((width_size,fixed_height))
        print("resizeeeeeed:",resized_image.size)
        from django.conf import settings
        resized_image.save("media/company_logo/"+logo.name)
        image_new1 = 'company_logo/'+logo.name
        tax_no = request.POST.get("tax_no",False)
        mobile_no = request.POST.get("mobile_no",False)
        website = request.POST.get("website",False)
        phone = request.POST.get("phone",False)
        email = request.POST.get("email",False)
        address = request.POST.get("address",False)
        now = datetime.now()

        data = company_master.objects.get(id=id)
        if (data.company_name != companyname or data.tax_number != tax_no or data.mobile != mobile_no  or data.website != website or data.phone != phone or data.email != email or data.address != address):
            update_status = True
        else:
            update_status = False
        if update_status == False :
            messages.error(request,"Not updated")
            return redirect(request.META['HTTP_REFERER'])
        else:

            current_time = now.strftime("%H:%M:%S")
            company_master.objects.filter(id=id).update(company_name = companyname,
                tax_number = tax_no,
                mobile = mobile_no,
                company_logo = image_new1,
                website = website,
                phone = phone,
                email = email,
                address = address,
                updated_by = request.user,
                updated_dt = date.today(),
                updated_tm = current_time

                )
            messages.success(request,"Successfully updated")
            return redirect(request.META['HTTP_REFERER'])




# -----------------------------------------------------user_management-----------------------------------------------------------------

def user_management(request):
    user_data = User.objects.all().first()
    member_data = User_details.objects.all().exclude(created_by = user_data)
    data = User_details.objects.all()
    context = {
        "data" : data,
        "member_data":member_data
    }
    return render(request, 'user_management.html',context)


@api_view(['POST'])
def user_management_action(request):
    data = request.data
    photo =  request.FILES['photo']
    fixed_height = 400
    image = Image.open(photo)
    print("image.size",image.size)
    width_size = int(fixed_height/image.height * image.width)
    resized_image = image.resize((width_size,fixed_height))
    print("resizeeeeeed:",resized_image.size)
    from django.conf import settings
    resized_image.save("media/user_image/"+photo.name)
    image_new1 = 'user_image/'+photo.name
    if data['password_option'] == "Automatic":
        import string    
        import random
        S = 10
        password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    else:
        password = request.POST.get("password",False)
    company_master_id = ''
    if User_details.objects.filter(username=data['username']).exists():
        messages.warning(request,"Username already exists")
        return redirect(request.META['HTTP_REFERER'])

    else:

        # super_admin add company admin(navabsir)

        if data['user_type'] == "company_admin":
            if company_master.objects.filter(company_name = data['companyname']).exists():
                company_model_data =company_master.objects.get(company_name = data['companyname'])
                company_master_id = company_model_data.id
            else:
                company_save = company_master.objects.create(company_name =data['companyname'],created_by = request.user,status="False")
                company_master_id = company_save.id
            user = User.objects.create_user(data['username'], password = password)
            user.save()
            user_data = User_details.objects.create(
                    company_id_id = company_master_id,
                    company_name =data['companyname'],
                    auth_user = user,
                    photo = photo,
                    name = data['name'],
                    username = data['username'],
                    password_option = data['password_option'],
                    password = password,
                    email = data['email'],
                    phone = data['phone'],
                    user_type = 'company_admin',
                    created_by = request.user,
                    status = "True"
                    )
            messages.success(request,"Successfully added User details")
            return redirect(request.META['HTTP_REFERER'])
            
        else:
            role_id = request.POST.getlist("role_id[]")
            
            role_description = request.POST.getlist("role_description[]")
            role_start_dt = request.POST.getlist("role_start_dt[]")
            role_end_dt = request.POST.getlist("role_end_dt[]")
            role_length = len(role_id)
            print("role_length::::::;",role_length)
            login_user_data = User_details.objects.get(auth_user=request.user)

            # company admin(navab sir) add company user senior(amar sir)

            if login_user_data.user_type == "company_admin":
                user = User.objects.create_user(data['username'], password = password)
                print("user_id::::;",user.id)
                user.save()
                user_data = User_details.objects.create(
                    company_id_id = login_user_data.company_id.id,
                    company_name =login_user_data.company_id.company_name,
                    auth_user = user,
                    photo = photo,
                    name = data['name'],
                    username = data['username'],
                    password_option = data['password_option'],
                    password = password,
                    email = data['email'],
                    phone = data['email'],
                    user_type = 'company_user',
                    created_by = request.user,
                    status = "True"
                    )
                data_save_active = user_active_account(user_id_id =user_data.id, active_user_id_id=login_user_data.id,active_auth_user_id_id=request.user.id)
                data_save_active.save()
                for i in range(0,role_length):
                    print("role_id::::::::::::",str(role_id))
                    print("role_id11::::::::::::",str(role_id[i]))
                    role_end_dt1 = role_end_dt[i]
                    if role_end_dt1 == "":
                        role_end_dt1 = None
                    data_save_user_role = user_permission_mapping(
                        auth_user_id = user,
                        user_id_id = user_data.id,
                        role_mapping_id_id = int(role_id[i]),
                        start_dt = role_start_dt[i],
                        end_dt = role_end_dt1,
                        description = role_description[i]
                    )
                    data_save_user_role.save()
                messages.success(request,"Successfully added new member")
                return redirect(request.META['HTTP_REFERER'])

            # company user senior(amar) add company user junior(Amritha)

            elif login_user_data.user_type == "company_user":
                user = User.objects.create_user(data['username'], password = password)
                user.save()
                user_data = User_details.objects.create(
                    company_id_id = login_user_data.company_id.id,
                    company_name =login_user_data.company_id.company_name,
                    auth_user = user,
                    photo = photo,
                    name = data['name'],
                    username = data['username'],
                    password_option = data['password_option'],
                    password = password,
                    email = data['email'],
                    phone = data['phone'],
                    user_type = 'company_user',
                    created_by = request.user,
                    status = "True"
                    )
                login_user_active_account = user_active_account.objects.get(user_id_id=login_user_data.id)
                print("login_user_active_account::::",str(login_user_active_account.id))
                data_save_active = user_active_account(user_id_id =user_data.id,active_user_id_id=login_user_active_account.active_user_id.id,active_auth_user_id_id=login_user_active_account.active_auth_user_id.id)
                data_save_active.save()
                for i in range(0,role_length):

                    role_end_dt1 = role_end_dt[i]
                    if role_end_dt1 == "":
                        role_end_dt1 = None
                    data_save_user_role = user_permission_mapping(
                        auth_user_id_id = user.id,
                        user_id_id = user_data.id,
                        role_mapping_id_id = role_id[i],
                        start_dt = role_start_dt[i],
                        end_dt = role_end_dt1,
                        description = role_description[i]
                    )
                    data_save_user_role.save()
                messages.success(request,"Successfully added new member")
                return redirect(request.META['HTTP_REFERER'])


def user_edit_modal_function(request):
    id = request.GET.get("id",False)
    data = User_details.objects.get(id=id)
    
    context = {
        "data" : data,
    }
    return render(request,'user_edit_modal_function.html',context)


def user_update_action(request):
     if request.method == "POST":
        id = request.POST.get("id",False)
        companyname = request.POST.get("companyname",False)
        photo =  request.FILES['photo']

        fixed_height = 400
        image = Image.open(photo)
        print("image.size",image.size)
        width_size = int(fixed_height/image.height * image.width)
        resized_image = image.resize((width_size,fixed_height))
        print("resizeeeeeed:",resized_image.size)
        from django.conf import settings
        resized_image.save("media/user_image/"+photo.name)
        image_new1 = 'user_image/'+photo.name

        name = request.POST.get("name",False)
        username = request.POST.get("username",False)
        password_option = request.POST.get("password_option",False)
        phone = request.POST.get("phone",False)
        email = request.POST.get("email",False)
        

        if password_option == "Automatic":
            import string    
            import random
            S = 10
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        else:
            password = request.POST.get("password",False)

        now = datetime.now()

        data = User_details.objects.get(id=id)
        if (data.company_name != companyname or data.name != name or data.username != username  or data.password_option != password_option or data.password != password or  data.phone != phone or data.email != email):
            update_status = True
        else:
            update_status = False
        if update_status == False :
            messages.error(request,"Not updated")
            return redirect(request.META['HTTP_REFERER'])
        else:

            current_time = now.strftime("%H:%M:%S")
            User_details.objects.filter(id=id).update(company_name = companyname,
                name = name,
                username = username,
                photo = image_new1,
                password_option = password_option,
                password = password,
                user_type = user_type,
                phone = phone,
                email = email,
                updated_by = request.user,
                updated_dt = date.today(),
                updated_tm = current_time

                )
            messages.success(request,"Successfully updated")
            return redirect(request.META['HTTP_REFERER'])



# -----------------------------------------------------member_management-----------------------------------------------------------------

def member_management(request):
    user_permission_modal = user_permission_mapping.objects.filter(auth_user_id=request.user)
    user_permission_modal1 = list(user_permission_modal.values_list('role_mapping_id',flat=True))
    user_manage_all_permission = Role_mapping.objects.filter(role_master_id__in=user_permission_modal1,navbar_name="Team member",manage_all=True)

    # print("user_manage_all_permission:::",str(user_manage_all_permission))
    today = date.today()
    user_data = User.objects.all().first()
    user_details_data = User_details.objects.get(auth_user=request.user)
    if user_manage_all_permission:
        active_user_id = user_active_account.objects.get(user_id_id=user_details_data.id)
        user_active_account1 = user_active_account.objects.filter(active_auth_user_id_id =active_user_id.active_auth_user_id )
        child_user_id = list(user_active_account1.values_list('user_id__auth_user',flat=True))
        child_user_id.append(int(active_user_id.active_auth_user_id.id))
        member_data = User_details.objects.filter(created_by__in=child_user_id).exclude(created_by = user_data)
    else:
        # user_active_account = user_active_account.objects.filter(active_auth_user_id =request.user )
        if user_details_data.user_type == "company_admin":
            user_active_account1 = user_active_account.objects.filter(active_auth_user_id =request.user )
            child_user_id = list(user_active_account1.values_list('user_id__auth_user',flat=True))
            child_user_id.append(int(request.user.id))
            member_data = User_details.objects.filter(created_by__in=child_user_id).exclude(created_by = user_data)
        else:
            member_data = User_details.objects.filter(created_by=request.user).exclude(created_by = user_data)

    role_data = Role_master.objects.all()

    # space_datas
    space_master_data = ""
    try:
        userdetails_data = User_details.objects.get(auth_user=request.user)

        # if user is company_admin (navab sir (all space of him))
        if userdetails_data.user_type == "company_admin":
            space_master_data = space_master.objects.filter(added_user_id=request.user)
    
        else:
            # if user is company_user(their space only)
            space_access_data = space_access_permission_user.objects.get(invite_user_auth_id=request.user)
            space_master_data = space_master.objects.filter(id=space_access_data.space_id.id)
    except:
        pass


    context = {
        "member_data" : member_data,
        "today":today,
        "role_data":role_data,
        "space_master_data":space_master_data
    }
    return render(request, 'member_management.html',context)


# -----------------------------------------------------space_management-----------------------------------------------------------------

def space_add_action(request):
    if request.method == "POST":
        spacename = request.POST.get("spacename",False)
        # if data['user_type'] == "company_admin":
        user_data = User_details.objects.get(auth_user = request.user)
        if user_data.user_type == "company_admin":
            space_master_data = space_master.objects.create(space_name=spacename,
            added_user_id = request.user,
            status = "True",
            created_by = request.user
            )
        else:
            user_active = user_active_account.objects.get(active_user_id=user_data.id)

            space_master_data = space_master.objects.create(space_name=spacename,
            active_account_id_id=user_active.active_user_id,
            added_user_id = request.user,
            status = "True",
            created_by = request.user
            )
       
        member_data = request.POST.getlist("member_data",False)
        
        for i in member_data:
            user_details = User_details.objects.get(id=i)
            space_access_permission_user.objects.create(space_id_id = space_master_data.id ,invite_user_details_id_id = i,invite_user_auth_id_id = user_details.auth_user.id)
        messages.success(request,"Successfully added Space")
        return redirect(request.META['HTTP_REFERER'])



# -----------------------------------------------------role_management-----------------------------------------------------------------

def role_management(request):
    data = Role_master.objects.all()
    user_data = User.objects.all().first()
    member_data = User_details.objects.all().exclude(created_by = user_data)

    space_master_data = ""
    try:
        userdetails_data = User_details.objects.get(auth_user=request.user)

        # if user is company_admin (navab sir (all space of him))
        if userdetails_data.user_type == "company_admin":
            space_master_data = space_master.objects.filter(added_user_id=request.user)
    
        else:
            # if user is company_user(their space only)
            space_access_data = space_access_permission_user.objects.get(invite_user_auth_id=request.user)
            space_master_data = space_master.objects.filter(id=space_access_data.space_id.id)
    except:
        pass

    context = {
        "member_data" : member_data,
        "data":data,
        "space_master_data":space_master_data
    }
    return render(request,"role_management.html",context)


def role_management_action(request):
    if request.method == "POST":
        data_save_role = Role_master.objects.create(
                role_name = request.POST.get('name'),
                description = request.POST.get('description'),
                status = "True",
                auth_user_id = request.user.id,
                created_by = request.user
            )

        Role_mapping.objects.create(
                role_master_id_id = data_save_role.id,
                navbar_name = "Company",
                read = request.POST.get('company_read',False),
                write = request.POST.get('company_write',False),
                edit = request.POST.get('company_edit',False),
                delete = request.POST.get('company_delete',False),
                view_all = request.POST.get('company_view_all',False),
                manage_all = request.POST.get('company_manage_all',False),
                created_by = request.user,
                status = "True"
            )

        Role_mapping.objects.create(
                role_master_id_id = data_save_role.id,
                navbar_name = "User",
                read =  request.POST.get('user_read',False),
                write =  request.POST.get('user_write',False),
                edit =  request.POST.get('user_edit',False),
                delete =  request.POST.get('user_delete',False),
                view_all =  request.POST.get('user_view_all',False),
                manage_all =  request.POST.get('user_manage_all',False),
                created_by = request.user,
                status = "True"
            )

        Role_mapping.objects.create(
                role_master_id_id = data_save_role.id,
                navbar_name = "Role",
                read = request.POST.get('role_read',False),
                write = request.POST.get('role_write',False),
                edit = request.POST.get('role_edit',False),
                delete = request.POST.get('role_delete',False),
                view_all = request.POST.get('role_view_all',False),
                manage_all = request.POST.get('role_manage_all',False),
                created_by = request.user,
                status = "True"
            )

        Role_mapping.objects.create(
                role_master_id_id = data_save_role.id,
                navbar_name = "Team member",
                read = request.POST.get('team_member_read',False),
                write = request.POST.get('team_member_write',False),
                edit = request.POST.get('team_member_edit',False),
                delete = request.POST.get('team_member_delete',False),
                view_all = request.POST.get('team_member_view_all',False),
                manage_all = request.POST.get('team_member_manage_all',False),
                created_by = request.user,
                status = "True"
            )

    messages.success(request,"Successfully added Role")
    return redirect(request.META['HTTP_REFERER'])




            
