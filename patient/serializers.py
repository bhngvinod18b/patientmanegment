from rest_framework import serializers
from .models import Patient, Appointment

class Patientserializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class Appointmentserializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'