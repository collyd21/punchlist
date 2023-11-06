from django import forms
from .models import Punch, PunchImage

class PunchForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Punch
        fields = ['title', 'description', 'complete', 'images']

