from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('completed', views.completed_task, name='completed_task'),
    path('remaining', views.remaining_task, name='remaining_task'),
    path('add', views.add_task, name='add_task'),
    path('delete/<str:task_id>', views.delete_task, name='delete_task'),
    path('detail/<str:task_id>', views.task_detail, name='task_detail'),
    path('toggle_complete/<str:task_id>', views.toggle_complete, name='toggle_complete'),
    path('remove_task/<str:task_id>', views.remove_task, name='remove_task'),
]