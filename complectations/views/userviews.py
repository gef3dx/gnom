from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from ..forms import UserCreationForm, UserUpdateForm


class UserViewList(LoginRequiredMixin, ListView):
    template_name = 'user/userlist.html'
    model = CustomUser
    paginate_by = 15
    context_object_name = 'users'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    
    def get_queryset(self, **kwargs):
        queryset = CustomUser.objects.all()
        return queryset
       

class UserAddView(LoginRequiredMixin, View):
    template_name = 'user/addusers.html'

    def get(self, request):
        if request.user.is_staff:
            context = {
                'form': UserCreationForm()
            }
            return render(request, self.template_name, context)
        else:
            return redirect('home')

    def post(self, request):
        if request.user.is_staff:
            form = UserCreationForm(request.POST)
    
            if form.is_valid():
                obj = form.save(commit=False)
                obj.username = request.POST["email"].split("@")[0]
                obj.save()
                return redirect('users')
            context = {
                'form': form
            }
            return render(request, self.template_name, context)
        else:
            return redirect('home')
        
class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "user/updateusers.html"
    model = CustomUser
    form_class = UserUpdateForm
    success_url = "/users"
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
        
class DelUserView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "user/daleteuser.html"
    success_url = "/users"
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            return redirect('home')
            
    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            self.object = None
            return super().post(request, *args, **kwargs)
        else:
            return redirect('home')
    