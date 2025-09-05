from django.shortcuts import render, redirect
from .forms import WatchForm
from .models import Watch
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

def home_view(request):
    template_name = "watch_app/home.html"
    context = {}
    return render(request, template_name, context)


@login_required(login_url='login')
def add_watch_view(request):
    form = WatchForm()
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail(
                'Test Email',
                'Hello! Your Product has been added.',
                'yogeshpandhargeri2022@gmail.com',  # From
                ['pandhargeri27@gmail.com'],  # To
                fail_silently=False,
            )

            messages.success(request, 'Watch Added Successfully')
            return redirect('show-watch')
    template_name = "watch_app/add_watch.html"
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login')
def show_watch_view(request):
    watches = Watch.objects.all()
    template_name = "watch_app/show_watch.html"
    context = {'watches': watches}
    return render(request, template_name, context)

def update_watch_view(request, id):
    watch = Watch.objects.get(id=id)
    form = WatchForm(instance=watch)
    if request.method == 'POST':
        form = WatchForm(request.POST,request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            send_mail(
                'Test Email',
                'Hello! Your Product has been updated.',
                'yogeshpandhargeri2022@gmail.com',  # From
                ['pandhargeri27@gmail.com'],  # To
                fail_silently=False,
            )
            messages.success(request, 'Watch Updated Successfully')
            return redirect('show-watch')
    template_name = "watch_app/add_watch.html"
    context = {'form': form}
    return render(request, template_name, context)

def delete_watch_view(request, id):
    watch = Watch.objects.get(id=id)
    watch.delete()
    send_mail(
        'Test Email',
        'Hello! Your Product has been Deleted.',
        'yogeshpandhargeri2022@gmail.com',  # From
        ['pandhargeri27@gmail.com'],  # To
        fail_silently=False,
    )
    messages.success(request, 'Watch Deleted Successfully')
    return redirect('show-watch')

def about_us_view(request):
    template_name = "watch_app/about_us.html"
    context = {}
    return render(request, template_name, context)

def contact_us_view(request):
    template_name = "watch_app/contact_us.html"
    context = {}
    return render(request, template_name, context)

