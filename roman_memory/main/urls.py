from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('links', views.about, name='links_home')
    # path('', include('main.urls')


]
