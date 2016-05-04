from django import forms

from .models import Documentation

class DocUploadForm(forms.ModelForm):
	'''Form for documentation file upload'''
	class Meta(object):
		model = Documentation
		fields = [
			"name",
			"doc_file",
		]
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Enter Title','class': 'form-control'}),
			'doc_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
		}
	doc_file = forms.FileField(
			label = 'Select a file',
			help_text = 'max. 5 megabytes',
		)
