import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_system.settings')
django.setup()

from django.contrib.auth.models import User, Group
from core.models import Appointment

def populate_mock_data():
    print("🚀 Injecting Base Users and Historical Data...")
    
    # 1. Setup Groups
    rec_group, _ = Group.objects.get_or_create(name='Receptionist')
    doc_group, _ = Group.objects.get_or_create(name='Doctor')

    # 2. Clear old test accounts to prevent duplicate errors
    User.objects.filter(username__in=['rec1', 'drsmith', 'drjones']).delete()
    Appointment.objects.all().delete() # Clear old appointments to start fresh
    
    # 3. Create Users
    rec_user = User.objects.create_user(username='rec1', password='password123')
    rec_user.groups.add(rec_group)
    print("✅ Created Receptionist: rec1 / password123")
    
    doc_user_smith = User.objects.create_user(username='drsmith', password='password123')
    doc_user_smith.groups.add(doc_group)
    print("✅ Created Doctor: drsmith / password123")

    doc_user_jones = User.objects.create_user(username='drjones', password='password123')
    doc_user_jones.groups.add(doc_group)
    print("✅ Created Doctor: drjones / password123")
    
    # 4. Create ONLY Historical Data for Patient "Robert M."
    now = timezone.now()
    
    # Visit 1 (60 days ago) - High Cholesterol
    Appointment.objects.create(
        patient_name="Robert M.", age=55, doctor=doc_user_smith,
        symptoms="Severe chest pain and shortness of breath.",
        appointment_datetime=now - timedelta(days=60), status='Completed',
        condition_notes="Patient reported high stress. Blood pressure elevated.",
        test_reports="Lipid Panel: 65% LDL Cholesterol (Dangerously High), Hemoglobin 45%.",
        prescription="Atorvastatin 40mg daily. Strict diet recommended."
    )
    
    # Visit 2 (30 days ago) - Improving
    Appointment.objects.create(
        patient_name="Robert M.", age=55, doctor=doc_user_smith,
        symptoms="Follow-up visit. Chest pain reduced.",
        appointment_datetime=now - timedelta(days=30), status='Completed',
        condition_notes="Patient strictly following diet. No recent chest pain episodes.",
        test_reports="Lipid Panel: 40% LDL Cholesterol (Improving). Hemoglobin 50%.",
        prescription="Continue Atorvastatin 40mg. Add daily 30-min cardio."
    )

    print("🎉 Success! Base data injected. Ready for live Demo.")

if __name__ == '__main__':
    populate_mock_data()