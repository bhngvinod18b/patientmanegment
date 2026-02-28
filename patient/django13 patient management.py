from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Appointment
from django.http import HttpResponse


def home(request):
    return render(request, 'patient/index.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient/list.html', {'patients': patients})
    
def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        if name and phone and description:
            Patient.objects.create(
                name=name, phone=phone, description=description
            )
            return redirect('patient:patient_list')# for GET requests, show empty form

    return render(request, 'patient/add.html')

def delete_patient(request, phone):
    patient = get_object_or_404(Patient, phone=phone)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient:home')
    return render(request, 'patient/delete.html', {'patient': patient})

def search_patient(request):
    patient = None
    if request.method == 'POST':
        phone = request.POST.get('phone')
        if phone:
            patient = Patient.objects.filter(phone=phone).first()
    return render(request, 'patient/search.html', {'patient': patient})
def add_appointments(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        department = request.POST.get('department')
        date = request.POST.get('date')
        time = request.POST.get('time')
        try:
            patient = Patient.objects.filter(phone=phone).first()
        except Patient.DoesNotExist:
            return (f" patient with this number {phone} does not exist")

        Appointment.objects.create(patient=patient, phone=phone, department=department, date=date,
                                   time=time)
        return redirect('patient:home')

    return render(request, 'patient/appointment.html')
def view_appointment(request):
    appointments = None
    if request.method == 'POST':
        phone = request.POST.get('phone')
        if not phone:
            return HttpResponse("phone number is required to get appointment", status=404)
        if phone:
            appointments = Appointment.objects.filter(phone=phone)
        
    
    return render(request, 'patient/list_appoint.html', {'appointments': appointments})
        
    

from rest_framework import viewsets
from .serializers import Patientserializers 
from .serializers import Appointmentserializers
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = Patientserializers
    lookup_field = 'phone'
    search_field = ['name', 'description']

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = Appointmentserializers
    lookup_field = 'phone'
    search_field = ['department', 'date']
    
