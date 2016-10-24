from django import forms

from .models import Documentation


class DocUploadForm(forms.ModelForm):
    '''Form for documentation file upload'''
    class Meta(object):
        model = Documentation
        fields = [
            "name",
            "doc_file",
            "description",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Title','class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description','class': 'form-control'}),
        }
