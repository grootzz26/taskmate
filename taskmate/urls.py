
from django.contrib import admin
from django.urls import path,include
from todolist_app import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo_views.home,name='home'),
    path('contact', todo_views.contact, name='contact'),
    path('about', todo_views.about, name='about'),
    path('', include('todolist_app.urls')),
    path('account/',include('users_app.urls')),
]
