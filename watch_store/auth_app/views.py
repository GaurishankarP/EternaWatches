from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    template_name = "auth_app/signup.html"
    context = {'form': form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login Successfully')
            return redirect('show-watch')

        else:
            messages.warning(request, 'Invalid Credentials')
    template_name = "auth_app/login.html"
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')