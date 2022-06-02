from django.shortcuts import render, redirect
from .models import Links
from .forms import LinksForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView



class LinksList(ListView):
    model = Links
    form_class = LinksForm
    template_name = 'links/links.html'
    context_object_name = 'links'
    success_url = '/links/'

def add_link(request):
    error = ''
    if request.method == 'POST':
        form = LinksForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return redirect('links')
        else:
            error = 'Форма введена не верно'
    form = LinksForm
    data = {'form': form,
            'error': error}
    return render(request, 'links/add_link.html', data)

class LinksDetailView(DetailView):
    model = Links
    template_name = 'links/link_detail.html'
    context_object_name = 'links'

class LinksRedactView(UpdateView):
    model = Links
    template_name = 'links/update_links.html'
    form_class = LinksForm

class LinksDeleteView(DeleteView):
    model = Links
    success_url = '/links/'
    template_name = 'links/delete_links.html'