from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_main, name='author_main'),


]
