from django import forms
from .models import Review

class RevForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating',  'anonymous', 'nickname')
        widgets = {
            'comment': forms.Textarea(attrs={
                'maxlength': '700',
            }),
        }
