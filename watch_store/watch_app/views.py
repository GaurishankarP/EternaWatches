from django.shortcuts import render, redirect
from .forms import WatchForm
from .models import Watch
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.db import models
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render
from .models import Watch

def home_view(request):
    User = get_user_model()



    if request.user.is_authenticated:
        # Show only watches belonging to the logged-in user
        watches = Watch.objects.filter(owner=request.user)
        total_watches = watches.count()
        total_brands = watches.values_list('brand', flat=True).distinct().count()
        total_users = User.objects.filter(is_staff=True).count()
        latest_watches = watches.order_by('-id')[:3]
    else:
        # For visitors (not logged in)
        watches = Watch.objects.none()
        total_watches = 0
        total_brands = 0
        total_users = User.objects.filter(is_staff=True).count()
        latest_watches = None

    template_name = "watch_app/home.html"
    context = {
        'watches': watches,
        'total_watches': total_watches,
        'total_brands': total_brands,
        'total_users': total_users,
        'latest_watches': latest_watches,
    }
    return render(request, template_name, context)



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

@login_required(login_url='login')
def add_watch_view(request):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            watch = form.save(commit=False)      # don't save yet
            watch.owner = request.user           # ✅ assign logged-in user
            watch.save()                         # now save
            send_mail(
                'Test Email',
                'Hello! Your Product has been added.',
                'yogeshpandhargeri2022@gmail.com',  # From
                ['pandhargeri27@gmail.com'],        # To
                fail_silently=False,
            )
            messages.success(request, 'Watch Added Successfully')
            return redirect('show-watch')
    else:
        form = WatchForm()

    return render(request, "watch_app/add_watch.html", {'form': form})


@login_required(login_url='login')
def show_watch_view(request):
    query = request.GET.get('q', '')
    watches = Watch.objects.filter(owner=request.user)
    if query:
        watches = watches.filter(
            models.Q(brand__icontains=query) |
            models.Q(name__icontains=query) |
            models.Q(model__icontains=query)
        )
    paginator = Paginator(watches, 8)  # 8 watches per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = "watch_app/show_watch.html"
    context = {
        'watches': page_obj.object_list,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'request': request,
    }
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

def faqs_view(request):
    template_name = "watch_app/faq.html"
    context = {}
    return render(request, template_name, context)

def privacy_policy_view(request):
    template_name = "watch_app/privacy_policy.html"
    context = {}
    return render(request, template_name, context)

def terms_and_conditions_view(request):
    template_name = "watch_app/terms_and_conditons.html"
    context = {}
    return render(request, template_name, context)


