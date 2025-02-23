from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
class SignupView(CreateView):
       form_class= UserCreationForm
       template_name='Home/register.html'
       success_url='smart/Notes'

       def get(self,request,*args,**kwargs):
              if self.request.user.is_authenticated:
                     return redirect('Notes.list')
              return super().get(request,*args,**kwargs)

class LoginInterfaceView(LoginView):
       template_name='Home/login.html'

class LogoutInterfaceView(LogoutView):
       template_name='Home/logout.html'

#class LogoutActionView(LogoutView):
 #   next_page = 'Home/logout.html'

class HomeView(TemplateView):
        template_name ='Home/Welcome.html'
