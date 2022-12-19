from django import forms

class InquiryForm(forms.Form):
    listing = forms.CharField()
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20, widget=forms.TextInput, required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
    user = forms.CharField()