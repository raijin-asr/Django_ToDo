from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('completed', views.completed_task, name='completed_task'),
    path('remaining', views.remaining_task, name='remaining_task'),
    path('add', views.add_task, name='add_task'),
    path('delete', views.delete_task, name='delete_task'),
    path('detail', views.task_detail, name='task_detail'),
]