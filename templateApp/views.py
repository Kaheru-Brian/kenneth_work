from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
from django.urls import reverse

# Create your views here.

days = {
    'monday': 'learn templating', 
    'tuesday': 'develop a django project',
    'wednesday': 'workout',
    'thursday': 'learn django',
    'friday': 'do templates',
    'saturday': 'learn static files',
    'sunday': 'rest'
}

def task(request):
    # todo = days.get(day)
    form = TaskForm()
    return render(request, 'templateApp/base.html',{'data':'todo', 'title':'day', 'form':form})



def index(request):
    return HttpResponse('Welcome to my To Do List!!')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        
        if form.is_valid():
            print('created')
            task_name = form.cleaned_data['name']
            details = form.cleaned_data['details']
            no_people= form.cleaned_data['no_people']
            date_created = form.cleaned_data['date_created']
            day_of_week = form.cleaned_data['day_of_week']
            Task.objects.create(name=task_name, details=details, no_people=no_people, date_created=date_created,day_of_week=day_of_week)
            return HttpResponseRedirect(reverse('indexpage'))
    else:
        form = TaskForm()
    task_list = Task.objects.all()   
    return render(request, 'templateApp/base.html',{ 'task_list':task_list, 'form':form})

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    redirect_url = reverse('create_task')
    return HttpResponseRedirect(redirect_url)

def edit_task(request, task_id):
    tasks = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['name']
            details = form.cleaned_data['details']
            no_people= form.cleaned_data['no_people']
            date_created = form.cleaned_data['date_created']
            day_of_week = form.cleaned_data['day_of_week']
            Task.objects.filter(id=task_id).update(name=task_name, details=details, no_people=no_people, date_created=date_created,day_of_week=day_of_week)

            # updating fields in the database.
            tasks.name = task_name
            tasks.details = details
            tasks.no_people = no_people
            tasks.date_created = date_created
            tasks.day_of_week = day_of_week
            tasks.save()
            redirect_url = reverse('create_task')
            return HttpResponseRedirect(redirect_url)
    else:
        form = TaskForm(initial={'name':tasks.name, 'details':tasks.details, 'no_people':tasks.no_people, 'date_created':tasks.date_created, 'day_of_week':tasks.day_of_week})
        return render(request, 'templateApp/edit_task.html', {'form':form, 'task_id':task_id})