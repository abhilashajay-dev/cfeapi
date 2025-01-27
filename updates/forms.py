from django import forms
from .models import Update as UpdateModel

class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = ['user','content', 'image']
    
    def clean(self, *args, **kwargs):
    	data = self.cleaned_data
    	content = self.data.get('content', None)
    	image = self.data.get('image', None)
    	if content == '' or content == "":
    		content = None

    	if content is None or image is None:
    		raise forms.ValidationError("content or image is required")

    	return super().clean(*args, **kwargs) 	