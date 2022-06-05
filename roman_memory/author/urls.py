from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_main, name='author_main'),
    path('error', views.author_error, name='author_error')


]
