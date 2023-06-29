from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor, Patient


class DoctorCreationForm(UserCreationForm):
    """The creation form for the custom user"""
    class Meta:
        model = Doctor
        fields = ['username']


class PatientForm(ModelForm):
    """A model form for a Patient record"""
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['doctor']

class DoctorForm(ModelForm):
    """A model form for a Doctor record"""
    class Meta:
        model = Doctor
        fields = ['username', 'email']