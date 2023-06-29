from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib import messages
from .forms import DoctorCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Patient, Doctor
from .forms import PatientForm, DoctorForm


level = (
        ('i', 'Intern'),
        ('m', 'Medical Practioner'),
        ('r', 'Registrar'),
        ('s', 'Specialist')
    )

def loginPage(request):
    """Handles login to the website"""
    """
    page variable determines which button is rendered
    between login or signup
    """
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = Doctor.objects.get(username=username)
        except:
            messages.error(request, 'Doctor entered does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password is incorrect')
    context = {'page': page}
    return render(request, 'patientClerk/login_signup.html', context)

def signupPage(request):
    """Sings up a new doctor to the site"""
    page = 'signup'
    form = DoctorCreationForm()
    if request.method == 'POST':
        form = DoctorCreationForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.username = doctor.username.lower()
            doctor.save()
            login(request, doctor)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during signup')
    context = {'form': form, 'page': page}
    return render(request, 'patientClerk/login_signup.html', context)

def logoutPage(request):
    """Logs the user out"""
    logout(request)
    return redirect('home')

def home(request):
    """Index"""
    doctors = Doctor.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    print('q: {}'.format(q))
    if len(q) == 1:
        patients = Patient.objects.filter(doctor__level__istartswith=q)
    else:
        patients = Patient.objects.filter(Q(working_diagnosis__icontains=q) | Q(summary__icontains=q))
    patient_count = patients.count()
    levels = level
    context = {'patients': patients, 'levels': levels, 'patient_count': patient_count,
               'doctors': doctors}
    return render(request, 'patientClerk/home.html', context)

def patient(request, pk):
    """Patients"""
    patient = Patient.objects.get(id=pk)
    levels = level
    context = {'patient': patient, 'levels': levels}
    return render(request, 'patientClerk/patient.html', context)

def userProfile(request, pk):
    """Creates the profile of a doctor"""
    doctor = Doctor.objects.get(id=pk)
    doctors = Doctor.objects.all()
    patients = doctor.patient_set.all()
    levels = level
    context = {'doctor': doctor, 'patients': patients, 'levels': levels, 'doctors': doctors}
    return render(request, 'patientClerk/profile.html', context)

@login_required(login_url='login')
def createPatient(request):
    """Creates a new Patient record"""
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.doctor = request.user
            patient.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'patientClerk/patient_form.html', context)

@login_required(login_url='login')
def updatePatient(request, pk):
    """Update existing patient history"""
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'patientClerk/patient_form.html', context)

@login_required(login_url='login')
def deletePatient(request, pk):
    """Deletes a Patient record from database"""
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('home')
    context = {'patient': patient}
    return render(request, 'patientClerk/delete_patient.html', context)

@login_required(login_url='login')
def updateUser(request):
    """Updates a user"""
    form = DoctorForm(instance=request.user)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=request.user.id)
    return render(request, 'patientClerk/update_user.html', {'form': form})