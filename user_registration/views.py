from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user_registration/user_created.html')
    else:
        form = UserForm()
    return render(request, 'user_registration/create_user.html', {'form': form})

def register_and_login(request):
    user_form = UserForm()
    login_form = LoginForm()
    if request.method == 'POST':
        if 'register_form_submit' in request.POST:
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                user = user_form.save() 
                auth_login(request, user)
                print("User email:", user.email)
                messages.success(request, 'User registered successfully!')
                return HttpResponseRedirect(request.path)
            
        elif 'login_form_submit' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('email')
                print(username)
                password = login_form.cleaned_data.get('password')
                print(password)
                user = authenticate(request, email=username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return HttpResponseRedirect('/users/profile/')  
                else:
                    print('Login fail')
                    login_form.add_error(None, 'Invalid username or password.')
    
    return render(request, 'user_registration/register_and_login.html', {'user_form': user_form, 'login_form': login_form})

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'user_registration/profile.html', {'user': user})

@login_required
def all_users(request):
    users = User.objects.all() 
    return render(request, 'user_registration/all_users.html', {'users': users})