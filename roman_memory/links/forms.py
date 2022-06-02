from .models import Links
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput, FileField



class LinksForm(ModelForm):
    class Meta:
        model = Links
        fields = ['title', 'text', 'link', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'},),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'}),
            'link': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка'}),
            'image': ClearableFileInput(attrs={
                'class': 'form-control',}),

        }
