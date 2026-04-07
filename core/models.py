from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient_name = models.CharField(max_length=150)
    age = models.IntegerField()
    symptoms = models.TextField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    appointment_datetime = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    # EHR Fields (Filled by Doctor)
    test_reports = models.TextField(blank=True, null=True, help_text="Lab results, vitals, percentages")
    condition_notes = models.TextField(blank=True, null=True)
    prescription = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.status}"