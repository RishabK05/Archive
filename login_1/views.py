from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import CreateView #For signing up new user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url="/smart/notes"

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}
  

class AuthorisedView(LoginRequiredMixin , TemplateView):
    template_name='home/authorize.html'
    login_url ='/admin'











""" def home(request):
    return render(request,'home/welcome.html',{'today':datetime.today()}) """



""" @login_required(login_url='/admin')
def authorized(request):
    return render(request,'home/authorize.html',{})
  """