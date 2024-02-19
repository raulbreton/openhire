from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from applicants.models import ApplicantProfile
from job_applications.models import JobApplication

@login_required
def applicant_dashboard(request, pk):
    # Obtener Datos
    applicant_profile = ApplicantProfile.objects.get(user_id=pk)
    applications = JobApplication.objects.filter(id=applicant_profile.id)

    context = {
        'applications': applications,
    }

    return render(request, 'applicant_dashboard.html', context)