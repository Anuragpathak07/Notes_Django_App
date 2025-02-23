from django import forms
from .models import notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = notes
        fields=('title','text')
        widgets={
            'title':forms.TextInput(attrs={'class': 'form-control my-3'}),
            'text':forms.Textarea(attrs={'class': 'form-control my-3'}),
        }
        labels={
            'text':'Write your thoughts'
        }   