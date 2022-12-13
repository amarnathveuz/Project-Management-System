from django.shortcuts import render

# Create your views here.

from .models import task

def index(request):
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