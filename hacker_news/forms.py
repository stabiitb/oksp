from django import forms

from .models import News, Comment


class NewsUploadForm(forms.ModelForm):
    """
    Form for news link upload
    """
    class Meta(object):
        model = News
        fields = [
            'title',
            'description',
            'link',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter Description', 'class': 'form-control'}),
            'link': forms.URLInput(attrs={'placeholder': 'For eg: https://www.google.co.in', 'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    Form for comment upload
    """
    class Meta(object):
        model = Comment
        fields = [
            'text',
        ]
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Comment', 'class': 'form-control'}),
        }
