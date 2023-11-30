from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from tasks.models import Tasks
from tasks.forms import TaskForm, TaskExplanationsForm
from complectations.models import Complectation
from django.shortcuts import redirect


class ObjectListView(LoginRequiredMixin, ListView):
    """Выводит все строительные объекты"""
    template_name = 'tasks/home.html'
    model = Complectation
    context_object_name = 'objects'
    paginate_by = 30
    queryset = Complectation.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Complectation.objects.all()
        else:
            queryset = Complectation.objects.filter(users=self.request.user)
        return queryset


class SingleTaskView(LoginRequiredMixin, DetailView):
    model = Tasks
    template_name = 'tasks/single.html'
    context_object_name = 'task'


class ExplanationsUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update.html'
    form_class = TaskExplanationsForm
    success_url = "/"


class ObjectUsersListView(LoginRequiredMixin, ListView):
    """Выводит всех закрепленных сотрудников за объектом"""
    template_name = 'tasks/objfromuser.html'
    model = Complectation
    context_object_name = 'users'
    paginate_by = 30

    def get_queryset(self, **kwargs):
        object_id = self.kwargs['object_id']
        if self.request.user.is_staff:
            return Complectation.objects.get(id=object_id).users.filter(role="Сотрудник")
        else:
            pass

    def get(self, request, *args, **kwargs):
        if self.request.user.role == "Сотрудник":
            return redirect('tasks')
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.request.user.role == "Сотрудник":
            return redirect('tasks')
        else:
            return super().get(request, *args, **kwargs)


class TaskUserListView(LoginRequiredMixin, ListView):
    """Выводит все задачи прораба по выбранному объекту"""
    template_name = 'tasks/tasks.html'
    model = Tasks
    context_object_name = 'tasks'
    paginate_by = 30

    def get_queryset(self, **kwargs):
        object_id = self.kwargs['object_id']

        if self.request.user.is_staff:
            user_id = self.kwargs['user_id']
            return Tasks.objects.filter(complectation__id=object_id, user__id=user_id)
        else:
            user_id = self.request.user.id
            return Tasks.objects.filter(complectation__id=object_id, user__id=user_id, status="В ходе выполнения")


class TasksCreateView(LoginRequiredMixin, CreateView):
    """Создает задачу прорабу по объекту"""
    template_name = "tasks/create.html"
    model = Tasks
    form_class = TaskForm
    success_url = "/tasks"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('hometask')

    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('hometask')


class TasksUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирует задачу прорабу по объекту"""
    template_name = "tasks/update.html"
    model = Tasks
    form_class = TaskForm
    success_url = "/tasks/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('hometask')

    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('hometask')


class TasksDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляет задачу прорабу по объекту"""
    model = Tasks
    template_name = "tasks/delete.html"
    success_url = "/tasks/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('hometask')

    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('hometask')
