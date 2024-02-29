from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . form import SignUpForm
from .models import Record

def index(request):
    records = Record.objects.all()

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
        return render(request, 'web/index.html',{'records': records})


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
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'Regitration successful..')
            return redirect('web:index')
    else:
        form = SignUpForm()   
        return render(request, 'web/register.html', {'form':form})

    return render(request, 'web/register.html', {'form':form})

# Single customer information
def customer_record(request, pk):
    if request.user.is_authenticated:
        cust_record = Record.objects.get(id=pk)
        return render(request, 'web/record.html', {'cust_record':cust_record})
    else:
        messages.success(request, 'Kindly login to view this information!')
        return redirect('web:index')

# deleting a signle record
def delete_record(request, pk):
    if request.user.is_authenticated:
        del_record = Record.objects.get(id=pk)
        del_record.delete()
        messages.success(request, 'Record has been successfully deleted')
        return redirect('web:index')
    else:
        messages.success(request, 'You must be logged in to delete this record.')
        return redirect('web:index')