from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import RegisterForm

def register(request):
    if request.method == 'POST':
        #sanitize form and register user
        form = RegisterForm(request.POST)
        if form.is_valid():
            #register user
            user = User.objects.create_user(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()
            #success message and redirect
            messages.success(request, 'Registration successful. Please log in')
            return redirect('login')
        else:
            form.errors
            return render(request, 'accounts/register.html', { 'form': form })
            
    else: 
        form = RegisterForm(request.POST) 
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        #login user
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')