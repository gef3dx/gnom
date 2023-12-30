from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from tasks.models import Tasks
from tasks.forms import TaskForm, TaskExplanationsForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from complectations.models import Complectation
from users.models import CustomUser
import datetime


class ObjectListView(LoginRequiredMixin, ListView):
    """Выводит все строительные объекты"""
    template_name = 'tasks/home.html'
    model = Complectation
    context_object_name = 'objects'
    queryset = Complectation.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Complectation.objects.all()
        else:
            queryset = Complectation.objects.filter(users=self.request.user)
        return queryset


class SingleTaskView(LoginRequiredMixin, DetailView):
    """Выводит заду и при нажатии на кнопку выполнить меняет статус задачи"""
    model = Tasks
    template_name = 'tasks/single.html'
    context_object_name = 'task'

    def post(self, request, *args, **kwargs):
        model_id = kwargs['pk']
        model_instance = get_object_or_404(Tasks, pk=model_id)
        # Обработка POST запроса
        model_instance.status = 'Выполнил'
        model_instance.save()
        # Добавление сообщения
        messages.success(request, 'Задача выполнена успешно.')
        # Перенаправление на страницу с подробностями объекта
        return redirect('home')




class ExplanationsUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update.html'
    form_class = TaskExplanationsForm
    success_url = "/"


class CompletedTaskView(LoginRequiredMixin,UpdateView):
    model = Tasks
    template_name = "Completed"

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

    def get_context_data(self, **kwargs):
        context = super(TaskUserListView, self).get_context_data(**kwargs)
        context['object_id'] = self.kwargs['object_id']
        context['user_id'] = self.kwargs['user_id']
        context['date_now'] = datetime.date.today()
        context['date_plus'] = datetime.date.today() + datetime.timedelta(days=7)
        return context


class TasksCreateView(LoginRequiredMixin, CreateView):
    """Создает задачу прорабу по объекту"""
    template_name = "tasks/create.html"
    model = Tasks
    form_class = TaskForm
    success_url = "/tasks"

    def form_valid(self, form):
        obj = form.save(commit=False)
        complectation = Complectation.objects.get(pk=self.kwargs['object_id'])
        obj.complectation = complectation
        user = CustomUser.objects.get(pk=self.kwargs['user_id'])
        obj.user = user
        return super(TasksCreateView, self).form_valid(form)

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
