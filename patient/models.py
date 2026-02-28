from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=1)
    phone = models.CharField(max_length=50)
    DEPARTMENT_CHOICES = [('CARDIOLOGY', 'CARDIOLOGY'),
                          ('DERMATOLOGY', 'DERMATOLOGY'),
                          ('NEWROLOGY', 'NEWROLOGY'),
                          ('NEPHROLOGY', 'NEPHROLOGY'),]
                          
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField()
    STETUS_CHOICES = [('PENDING', 'PENDING'),
                      ('NOT DONE', 'NOT DONE'), 
                      ('DONE', 'DONE')]
    stetus = models.CharField(max_length=100, choices=STETUS_CHOICES, default='NOT DONE')
    def __str__(self):
        return self.name