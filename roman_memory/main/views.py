from django.shortcuts import render

def index(request):
    return render(request, 'main/main_menu.html')

def about(request):
    return render(request, 'main/links.html')