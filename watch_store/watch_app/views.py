from django.shortcuts import render, redirect
from .forms import WatchForm
from .models import Watch
from django.contrib.auth.decorators import login_required

def home_view(request):
    template_name = "watch_app/home.html"
    context = {}
    return render(request, template_name, context)


@login_required(login_url='login')
def add_watch_view(request):
    form = WatchForm()
    if request.method == 'POST':
        form = WatchForm(request.POST)
        if form.is_valid():
            form.save()
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
        form = WatchForm(request.POST, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('show-watch')
    template_name = "watch_app/add_watch.html"
    context = {'form': form}
    return render(request, template_name, context)

def delete_watch_view(request, id):
    watch = Watch.objects.get(id=id)
    watch.delete()
    return redirect('show-watch')

