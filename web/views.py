from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . form import SignUpForm

def index(request):
     
    #checking if the user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate the user
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('web:index')
        else:
            messages.success(request, 'An error occured, please try again')
            return redirect('web:index')

    else:
        return render(request, 'web/index.html',{})


def user_login(request):
    pass


def user_logout(request):
    logout(request)
    messages.success(request, " You've been logged out!")
    return redirect('web:index')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Regitration successful..')
            return redirect('web:index')
    else:
        form = SignUpForm()

    return render(request, 'web/register.html', {'form':form})