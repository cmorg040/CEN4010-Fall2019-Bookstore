from django import forms

class GenreBrowseForm(forms.Form):
    genre = forms.CharField(label='genre', max_length=100)