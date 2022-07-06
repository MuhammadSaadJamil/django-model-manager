from django import forms
from .models import Object


class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = "__all__"
        exclude = ("is_available",)
