from django import forms
from .models import obituary_platform

class ObituaryForm(forms.ModelForm):
	class Meta:
		model = obituary_platform
		fields = ['name', 'date_of_birth', 'date_of_death', 'content', 'author', 'slug']
    
