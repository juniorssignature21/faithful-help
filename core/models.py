from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
SERVICE_CHOICES = (
    ('___','Service'),
    ("home_based_elderly_care", "Home-Based Elderly Care"),
    ("hospital_support_care", "Hospital Support Care"),
    ("free_medical_outreach", "Free Medical Outreach"),
    ("caregiver_training", "Caregiver Training"),
    ("international_career_preparation", "International Career Preparation"),
    ("professional_certification", "Professional Certification"),
)
PREFERRED_CAREGIVING_EXPERIENCE = (
    ('___','Preferred Caregiving Experience'),
    ('elderly_care_specialist', 'Elderly Care Specialist'),
    ('nursing_assistant', 'Nursing Assistant'),
    ('companion_care', 'Companion Care')
)
class Contact(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
class Appointment(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True, choices=SERVICE_CHOICES)
    caregiver_experience = models.CharField(max_length=255, blank=True,null=True, choices=PREFERRED_CAREGIVING_EXPERIENCE)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    special_request = models.TextField(max_length=500, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Appointment for {self.service} with a {self.caregiver_experience} Experience"
    