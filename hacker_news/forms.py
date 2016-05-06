from django import forms

from .models import New


class NewsUploadForm(forms.ModelForm):
    '''Form for news link upload'''
    class Meta(object):
        model = New
        fields = [
            'title',
            'link',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title','class': 'form-control'}),
            'link': forms.URLInput(attrs={'placeholder': 'For eg: https://www.google.co.in', 'class': 'form-control'}),
        }
