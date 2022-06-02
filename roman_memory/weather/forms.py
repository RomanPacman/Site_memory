from .models import City_weather
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput, FileField


class CitiesForm(ModelForm):
    class Meta:
        model = City_weather
        fields = ['name']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название города'}, )
        }