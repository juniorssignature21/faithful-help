from django import forms
from core import models as core_models


class CreateContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}), required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Subject'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}), required=True)
    class Meta:
        model = core_models.Contact
        fields = ['full_name', 'email', 'phone', 'subject', 'message']
        
        
class BookAppointmentForm(forms.ModelForm):
    
    service = forms.ChoiceField(
        choices=core_models.SERVICE_CHOICES,
        widget=forms.Select()
    )
    caregiver_experience = forms.ChoiceField(
        choices=core_models.PREFERRED_CAREGIVING_EXPERIENCE,
        widget=forms.Select()
    )
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone'}), required=True)
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date'
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type':'time'
    }))
    special_request = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Special Request'
    }))
    
    class Meta:
        model = core_models.Appointment
        fields = "__all__"
        exclude = ['created_at', 'updated_at']
        