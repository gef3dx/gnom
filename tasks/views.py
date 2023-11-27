from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Tasks
from tasks.forms import TaskForm
from complectations.models import Complectation


class ObjectListView(LoginRequiredMixin, ListView):
    """Выводит все строительные объекты"""
    template_name = 'tasks/home.html'
    model = Complectation
    context_object_name = 'objects'
    paginate_by = 30
    queryset = Complectation.objects.all()


class ObjectUsersListView(LoginRequiredMixin, ListView):
    """Выводит всех закрепленных сотрудников за объектом"""
    template_name = 'tasks/objfromuser.html'
    model = Complectation
    context_object_name = 'users'
    paginate_by = 30

    def get_queryset(self, **kwargs):
        object_id = self.kwargs['object_id']
        return Complectation.objects.get(id=object_id).users.filter(role="Сотрудник")


class TaskUserListView(LoginRequiredMixin, ListView):
    """Выводит все задачи прораба по выбранному объекту"""
    template_name = 'tasks/tasks.html'
    model = Tasks
    context_object_name = 'tasks'
    paginate_by = 30

    def get_queryset(self, **kwargs):
        print(self.request)
        object_id = self.kwargs['object_id']
        user_id = self.kwargs['user_id']
        return Tasks.objects.filter(complectation__id=object_id, user__id=user_id)


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
