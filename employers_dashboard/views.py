from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from employers.models import EmployerProfile
from job_offers.models import JobOffer
from job_applications.models import JobApplication
from applicants.models import ApplicantProfile

@login_required
def job_offers(request, pk):
    if not request.user.is_authenticated or not request.user.is_employer:
        return redirect('login')  # Redirect to login if the user is not an employer
    
    # Obtener Datos
    employer_profile = EmployerProfile.objects.get(user_id=pk)
    job_offers = JobOffer.objects.filter(employer_profile=employer_profile)

    context = {
        'job_offers': job_offers,
    }

    return render(request, 'employer_dashboard.html', context)

def job_applications(request, job_offer_id):
    applications = JobApplication.objects.filter(job_offer_id=job_offer_id)

    if not applications:
        message = "No hay aplicaciones para esta oferta de trabajo en este momento."
        return render(request, 'job_applicants.html', {'message': message})

    return render(request, 'job_applicants.html', {'applications': applications})

def application_details(request, application_id):
    application = JobApplication.objects.get(id=application_id)

    return render(request, 'application_detail.html', {'application':application})

def applicant_details(request, application_id):
    applicant = ApplicantProfile.objects.get(id=application_id)

    return render(request, 'applicant_details.html', {'applicant':applicant})