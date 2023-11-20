from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tasks.models import Tasks
from tasks.forms import TaskForm


class TasksReadListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/home.html'
    model = Tasks
    paginate_by = 30
    context_object_name = 'tasks'


class TasksCreateView(LoginRequiredMixin, CreateView):
    template_name = "tasks/create.html"
    model = Tasks
    form_class = TaskForm
    # success_url = "/"


class TasksUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "tasks/update.html"
    model = Tasks
    form_class = TaskForm
    # success_url = "/"


class TasksDeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = "tasks/delete.html"
    # success_url = "/"
