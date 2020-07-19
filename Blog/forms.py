from django import forms
from .models import Blog, Author


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['Title', 'Description']

        widgets = {
            'Title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'Description': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }


class Authorform(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }
