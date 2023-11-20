from django.contrib.auth import authenticate, login
from django import views
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages

class LoginView(views.View):
     
     temolate_name = 'registration/login.html'
     success_url = reverse_lazy('/1')

     def post(self, request):
          email = request.POST['email']
          password = request.POST['password']
          user = authenticate(request, email=email, password=password)
          if user is not None:
               login(request, user)
               return redirect(self.success_url)
          else:
               messages.error(request, 'Invalid email or password')
               return render(request, self.temolate_name)

          


