from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_home, name='notes_home'),
    path('add_note', views.add_note, name='add_note'),
    path('<int:pk>', views.NotesDetailView.as_view(), name='note_detail'),
    path('<int:pk>/redact', views.NotesRedactView.as_view(), name='note_redact'),
    path('<int:pk>/delete', views.NotesDeleteView.as_view(), name='note_delete')

]
