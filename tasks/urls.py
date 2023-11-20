from django.urls import path
from tasks.views import TasksReadListView, TasksCreateView, TasksUpdateView, TasksDeleteView

urlpatterns = [
    path('', TasksReadListView.as_view(), name='hometask'),
    path('add/', TasksCreateView.as_view(), name='addtask'),
    path('update/<int:pk>/', TasksUpdateView.as_view(), name='updatetask'),
    path('delete/<int:pk>/', TasksDeleteView.as_view(), name='deletetask'),
]
