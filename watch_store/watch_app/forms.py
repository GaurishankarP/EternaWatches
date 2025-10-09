from django import forms
from .models import Watch

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = "__all__"
        exclude = ['owner']