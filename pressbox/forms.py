from django import forms

class PressItemForm(forms.ModelForm):
    short_description = forms.CharField(widget=forms.Textarea())
