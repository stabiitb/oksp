from django import forms

from .models import News


class NewsUploadForm(forms.ModelForm):
    '''Form for news link upload'''
    class Meta(object):
        model = News
        fields = [
            'title',
            'link',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title','class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
        }
