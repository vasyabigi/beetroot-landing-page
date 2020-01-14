from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(label="", max_length=2)
    message = forms.CharField(label='Message', widget=forms.Textarea)
