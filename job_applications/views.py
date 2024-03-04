from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from job_offers.models import JobOffer
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from .models import JobApplication

def apply_for_job(request, job_offer_id):
    if not request.user.is_authenticated or not request.user.is_applicant:
        return redirect('login')  # Redirect to login if the user is not an employer
    
    job_offer = JobOffer.objects.get(pk=job_offer_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.clean()
            try:
                # Save the application to the database
                application = form.save(commit=False)
                application.candidate = request.user.applicantprofile
                application.job_offer = job_offer
                application.save()
                # Redirect to the home page
                return redirect('applicants-home')
            except IntegrityError:
                form.add_error(None, "Ya aplicaste para este trabajo")
    else:
        form = JobApplicationForm()

    return render(request, 'job_application.html', {'form': form, 'job_offer': job_offer})

def delete_application(request, pk):
    application_instance = get_object_or_404(JobApplication, id=pk)
    application_instance.delete()
    
    return redirect('applicants-home')

def set_status(request, pk, status):
    application = get_object_or_404(JobApplication, id=pk)

    # Cambia el campo 'status' de la aplicación a 'Rechazado'
    application.status = status
    application.save()

    # Redirige a la página del dashboard del empleador o a donde desees
    return redirect('employers-home')