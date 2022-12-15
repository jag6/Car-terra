from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from . forms import RegisterForm, LoginForm

#register page
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            #sanitize form and register user
            user = User.objects.create_user(first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()
            #success message and redirect
            messages.success(request, 'Registration successful. Please log in')
            return redirect('login')
        else:
            #output any errors
            form.errors
            return render(request, 'accounts/register.html', { 'form': form })
            
    else: 
        form = RegisterForm(request.POST) 
        return render(request, 'accounts/register.html')

#login page
def login(request):
    #head tags
    title = 'Login'
    description = 'Login page'
    image = '/static/images/login-banner.jpg'
    url = '/accounts/login'
    
    form = LoginForm(request.POST)
    
    context = { 
                'title': title,
                'description': description,
                'image': image,
                'url': url,
                'form': form
            }
    
    if request.method == 'POST':
        if form.is_valid():
            #sanitize form and validate user
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is None:
                messages.error(request, 'Invalid credentials, please try again')
                return render(request, 'accounts/login.html', context)  
            else: 
                #success message and redirect
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials, please try again')
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, 'accounts/login.html', context)

#logout method
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logout Successful')
        return redirect('login')

#user dashboard page
def dashboard(request):
    #head tags
    title = 'Dashboard'
    description = 'Dashboard page'
    image = '/static/images/dashboard-banner.jpg'
    url = '/accounts/dashboard'
    
    context = { 
                'title': title,
                'description': description,
                'image': image,
                'url': url
            }
    
    return render(request, 'accounts/dashboard.html', context)