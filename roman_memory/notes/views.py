from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def notes_home(request):
    notes = Notes.objects.order_by('-date')
    return render(request, 'notes/notes.html', {'notes': notes})


class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'


class NotesRedactView(UpdateView):
    model = Notes
    template_name = 'notes/edit_note.html'
    form_class = NotesForm


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/notes/'
    template_name = 'notes/delete_note.html'


def add_note(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('notes_home')
        else:
            error = 'Форма введена не верно'
    form = NotesForm
    data = {'form': form,
            'error': error}
    return render(request, 'notes/add_note.html', data)
