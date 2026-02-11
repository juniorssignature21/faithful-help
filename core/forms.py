from django import forms
from .models import Contact


class CreateContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Subject'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}), required=True)
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'subject', 'message']