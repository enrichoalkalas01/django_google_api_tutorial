from django import urls
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from .import views

app_name = "users"

urlpatterns = [
    path('', include('main.urls', namespace="main"))
    path('', include('users.urls', namespace="users"))
    path('admin/', admin.site.urls)
]