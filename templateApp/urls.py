from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.index, name='indexpage'),
    path('day', views.task, name='task'),
    path('create', views.create_task, name='create_task'),
    path('delete/<int:task_id>', views.delete_task, name='delete_task'),
    path('update/<int:task_id>', views.edit_task, name='edit_task'),
   
    
   
]