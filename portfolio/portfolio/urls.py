from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to my portfolio as a aspiring Django Developer")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', welcome),
]
