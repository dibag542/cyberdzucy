from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['anons', 'full_text', 'date']

        widgets = {
            "anons": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Краткое описание проблемы"
            }),
            "date": DateTimeInput(attrs={
                'type':'date',
                'class': "form-control",
                'placeholder': "Дата отправки"
            }),
            "full_text": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Описание ваших действий(если не предпринимали ничего, то поставьте минус)"
            })
        }

