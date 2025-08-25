from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
            return redirect('show-watch')
    template_name = "auth_app/login.html"
    context = {}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('login')