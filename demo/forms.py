from django import forms

from .models import InputImage


class InputImageForm(forms.ModelForm):
    class Meta:
        model = InputImage
        fields = ("title", "input_image")
