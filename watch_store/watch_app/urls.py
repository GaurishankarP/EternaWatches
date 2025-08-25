from django.urls import path
from .views import home_view, add_watch_view, show_watch_view, update_watch_view, delete_watch_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('add/',add_watch_view, name="add-watch"),
    path('show/',show_watch_view, name="show-watch"),
    path('update/<id>',update_watch_view, name="update-watch"),
    path('delete/<id>',delete_watch_view, name="delete-watch"),
]