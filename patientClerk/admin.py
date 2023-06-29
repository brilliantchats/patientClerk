from django.contrib import admin
from .models import Doctor, Patient
from .forms import DoctorCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class DoctorAdmin(UserAdmin):
    """The admin class for custom user"""
    model = Doctor
    add_form = DoctorCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Optional Info',
            {
                'fields': (
                    'mdpcz_reg',
                    'institution',
                    'contacts',
                    'level',
                )
            }
        )
    )
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
