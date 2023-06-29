from django.db import models

from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class Doctor(AbstractUser):
    """
    This is the  custom user model, inherits from default User model
    """
    mdpcz_reg = models.CharField(max_length=20, null=True, blank=True, unique=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    contacts = models.CharField(max_length=20, null=True, blank=True)

    specialisation = (
        ('i', 'Intern'),
        ('m', 'Medical Practioner'),
        ('r', 'Registrar'),
        ('s', 'Specialist')
    )

    level = models.CharField(
        max_length=200,
        choices= specialisation,
        blank=True,
        default='m',
        help_text='Your current level of specialisation',
    )
    def get_absolute_url(self):
        """Returns an URL to access a detail view of doctor"""
        return reverse('doctor-detail', args=[str(self.id)])
    
    def __str__(self):
        """String representaion"""
        return self.username
    

class Patient(models.Model):
    """Represents a Patient record"""
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=(('m', 'Male'), ('f', 'Female')))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    presenting_complaint = models.CharField(max_length=200)
    hx_presenting_complaint = models.TextField(null=True, blank=True)
    systems_review = models.TextField(null=True, blank=True)
    past_medical_hx = models.TextField(null=True, blank=True)
    family_social = models.TextField(null=True, blank=True)
    general_exam = models.TextField()
    cardiovascular_exam = models.TextField(null=True, blank=True)
    respiratory_exam = models.TextField(null=True, blank=True)
    abdominal_exam = models.TextField(null=True, blank=True)
    neurological_exam = models.TextField(null=True, blank=True)
    summary = models.TextField()
    working_diagnosis = models.CharField(max_length=200)
    differentials = models.TextField(null=True, blank=True)
    management = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        """String representation"""
        return self.summary
    
    def get_absolute_url(self):
        """Returns an URL to access a detail view of patient"""
        return reverse('doctor-detail', args=[str(self.id)])
