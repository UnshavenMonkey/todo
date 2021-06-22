from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import TaskUserLoginForm, TaskUserRegisterForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    title = 'Join in'
    login_form = TaskUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    content = {'title': title, 'login_form':login_form}
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))     


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = TaskUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = TaskUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)
    
    
def edit(request):
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
