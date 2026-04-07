from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Appointment
from django.utils import timezone


@login_required
def home_router(request):
    if request.user.groups.filter(name='Receptionist').exists():
        return redirect('receptionist_dashboard')
    elif request.user.groups.filter(name='Doctor').exists():
        return redirect('doctor_dashboard')
    return render(request, 'core/error.html', {'msg': 'No role assigned.'})

@login_required
def receptionist_dashboard(request):
    # THE FIX: Only fetch appointments for TODAY and the future.
    # This automatically hides all past historical data from the receptionist!
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    appointments = Appointment.objects.filter(appointment_datetime__gte=today_start).order_by('appointment_datetime')
    alerts = Appointment.objects.filter(status='Rejected')
    doctors = User.objects.filter(groups__name='Doctor')

    if request.method == 'POST':
        doc_id = request.POST.get('doctor_id')
        dt = request.POST.get('datetime')
        
        if Appointment.objects.filter(doctor_id=doc_id, appointment_datetime=dt).exclude(status__in=['Cancelled', 'Rejected']).exists():
            messages.error(request, "CLASH: Doctor is busy at this time!")
        else:
            appt_id = request.POST.get('appointment_id')
            if appt_id:
                appt = Appointment.objects.get(id=appt_id)
                appt.doctor_id = doc_id
                appt.appointment_datetime = dt
                appt.status = 'Pending'
                appt.save()
            else:
                Appointment.objects.create(
                    patient_name=request.POST.get('patient_name'),
                    age=request.POST.get('age'),
                    symptoms=request.POST.get('symptoms'),
                    doctor_id=doc_id,
                    appointment_datetime=dt
                )
            messages.success(request, "Appointment secured.")
        return redirect('receptionist_dashboard')

    return render(request, 'core/receptionist_dashboard.html', {'appointments': appointments, 'alerts': alerts, 'doctors': doctors})
    appointments = Appointment.objects.all().order_by('-appointment_datetime')
    alerts = Appointment.objects.filter(status='Rejected')
    doctors = User.objects.filter(groups__name='Doctor')

    if request.method == 'POST':
        doc_id = request.POST.get('doctor_id')
        dt = request.POST.get('datetime')
        
        if Appointment.objects.filter(doctor_id=doc_id, appointment_datetime=dt).exclude(status__in=['Cancelled', 'Rejected']).exists():
            messages.error(request, "CLASH: Doctor is busy at this time!")
        else:
            # Check if this is a reschedule (updating an old record) or a new one
            appt_id = request.POST.get('appointment_id')
            if appt_id:
                appt = Appointment.objects.get(id=appt_id)
                appt.doctor_id = doc_id
                appt.appointment_datetime = dt
                appt.status = 'Pending'
                appt.save()
            else:
                Appointment.objects.create(
                    patient_name=request.POST.get('patient_name'),
                    age=request.POST.get('age'),
                    symptoms=request.POST.get('symptoms'),
                    doctor_id=doc_id,
                    appointment_datetime=dt
                )
            messages.success(request, "Appointment secured.")
        return redirect('receptionist_dashboard')

    return render(request, 'core/receptionist_dashboard.html', {'appointments': appointments, 'alerts': alerts, 'doctors': doctors})

@login_required
def doctor_dashboard(request):
    patients = Appointment.objects.filter(doctor=request.user, status__in=['Pending', 'Accepted']).order_by('appointment_datetime')
    return render(request, 'core/doctor_dashboard.html', {'patients': patients})

@login_required
def update_status(request, pk, new_status):
    appt = get_object_or_404(Appointment, pk=pk)
    appt.status = new_status
    appt.save()
    return redirect('doctor_dashboard')

@login_required
def write_prescription(request, pk):
    visit = get_object_or_404(Appointment, pk=pk)
    
    # THE FIX: Smart History Fetching. 
    # Uses '__icontains' so "Robert" will match "Robert M.", and filters by Age.
    history = Appointment.objects.filter(
        patient_name__icontains=visit.patient_name, 
        age=visit.age,
        status='Completed'
    ).exclude(pk=pk).order_by('-appointment_datetime')

    if request.method == 'POST':
        visit.condition_notes = request.POST.get('condition')
        visit.test_reports = request.POST.get('test_reports')
        visit.prescription = request.POST.get('prescription')
        visit.status = 'Completed'
        visit.save()
        return redirect('doctor_dashboard')

    return render(request, 'core/consultation.html', {'visit': visit, 'history': history})
    visit = get_object_or_404(Appointment, pk=pk)
    # The Smart History Query
    history = Appointment.objects.filter(patient_name=visit.patient_name, status='Completed').exclude(pk=pk)

    if request.method == 'POST':
        visit.condition_notes = request.POST.get('condition')
        visit.test_reports = request.POST.get('test_reports') # <-- Added this line
        visit.prescription = request.POST.get('prescription')
        visit.status = 'Completed'
        visit.save()
        return redirect('doctor_dashboard')

    return render(request, 'core/consultation.html', {'visit': visit, 'history': history})

@login_required
def view_prescription(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    return render(request, 'core/prescription_pdf.html', {'appointment': appt})
