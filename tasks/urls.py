from django.urls import path
from tasks.views import TasksCreateView, TasksUpdateView, TasksDeleteView, ObjectFromUserListView, UserListView, \
    TaskForObjectAndUser

urlpatterns = [
    path('', UserListView.as_view(), name='hometask'),
    path('user/<int:user_id>/', ObjectFromUserListView.as_view(), name='objects'),
    path('user/<int:user_id>/object/<int:object_id>/', TaskForObjectAndUser.as_view(), name='tasks'),
    path('add/', TasksCreateView.as_view(), name='addtask'),
    path('update/<int:pk>/', TasksUpdateView.as_view(), name='updatetask'),
    path('delete/<int:pk>/', TasksDeleteView.as_view(), name='deletetask')
]
