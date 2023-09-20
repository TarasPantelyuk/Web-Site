from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'П.І.Б'}),
            "anons": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефону'}),
            "date": TextInput(attrs={'class': 'form-control', 'placeholder': 'Місто'}),
            "full_text": TextInput(attrs={'class': 'form-control', 'placeholder': 'Відділення'})
        }