from .models import Notes
from django.forms import ModelForm, TextInput, Textarea


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'}),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'}),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст записи'}),


        }