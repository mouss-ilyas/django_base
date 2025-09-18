# myapp/forms.py
from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['text_field', 'number_field', 'image_field', 'audio_field']
