from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Tasks
from tasks.forms import TaskForm
from complectations.models import Complectation
from users.models import CustomUser


class UserListView(LoginRequiredMixin, ListView):
    """Выводит всех прорабов"""
    template_name = 'tasks/home.html'
    model = CustomUser
    context_object_name = 'users'
    paginate_by = 30
    queryset = CustomUser.objects.filter(is_worker=True)


class ObjectFromUserListView(LoginRequiredMixin, ListView):
    """Выводит объекты прораба"""
    template_name = 'tasks/objfromuser.html'
    model = Complectation
    context_object_name = 'objects'
    paginate_by = 30

    def get_queryset(self, **kwargs):
        user_id = self.kwargs['user_id']
        return Complectation.objects.filter(prorab__id=user_id)


class TaskForObjectAndUser(LoginRequiredMixin, ListView):
    """Выводит все задачи прораба по выбранному объекту"""
    template_name = 'tasks/tasks.html'
    model = Tasks
    context_object_name = 'tasks'
    paginate_by = 30

    def get_queryset(self, **kwargs):
        user_id = self.kwargs['user_id']
        object_id = self.kwargs['object_id']
        return Tasks.objects.filter(user__id=user_id, complectation__id=object_id)


class TasksCreateView(LoginRequiredMixin, CreateView):
    """Создает задачу прорабу по объекту"""
    template_name = "tasks/create.html"
    model = Tasks
    form_class = TaskForm
    success_url = "/"


class TasksUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирует задачу прорабу по объекту"""
    template_name = "tasks/update.html"
    model = Tasks
    form_class = TaskForm
    success_url = "/tasks/"


class TasksDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляет задачу прорабу по объекту"""
    model = Tasks
    template_name = "tasks/delete.html"
    success_url = "/tasks/"
