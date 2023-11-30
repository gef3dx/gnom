from django.urls import path
from tasks.views import TasksCreateView, TasksUpdateView, TasksDeleteView, ObjectListView, ObjectUsersListView,\
    TaskUserListView, SingleTaskView

urlpatterns = [
    path('', ObjectListView.as_view(), name='hometask'),
    path('object/<int:object_id>/', ObjectUsersListView.as_view(), name='objuser'),
    path('object/<int:object_id>/user/<int:user_id>/', TaskUserListView.as_view(), name='tasks'),
    path('task/<int:pk>/', SingleTaskView.as_view(), name='singletask'),
    path('add/', TasksCreateView.as_view(), name='addtask'),
    path('update/<int:pk>/', TasksUpdateView.as_view(), name='updatetask'),
    path('delete/<int:pk>/', TasksDeleteView.as_view(), name='deletetask')
]
