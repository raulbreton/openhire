from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from employers.models import EmployerProfile
from job_offers.models import JobOffer
from job_applications.models import JobApplication

@login_required
def job_offers(request, pk):
    # Obtener Datos
    employer_profile = EmployerProfile.objects.get(user_id=pk)
    job_offers = JobOffer.objects.filter(employer_profile=employer_profile)

    context = {
        'job_offers': job_offers,
    }

    return render(request, 'employer_dashboard.html', context)

def job_applications(request, pk, job_offer_id):
    employer_profile = EmployerProfile.objects.get(user_id=pk)
    job_offers = JobOffer.objects.filter(employer_profile=employer_profile)
    applications = JobApplication.objects.filter(job_offer_id=job_offer_id)

    context = {
        'job_offers': job_offers,
        'applications': applications,
    }

    return render(request, 'employer_dashboard.html', context)

def application_details(request, pk, job_offer_id, application_id):
    employer_profile = EmployerProfile.objects.get(user_id=pk)
    job_offers = JobOffer.objects.filter(employer_profile=employer_profile)
    applications = JobApplication.objects.filter(job_offer_id=job_offer_id)
    application = JobApplication.objects.get(id=application_id)

    context = {
        'job_offers':job_offers,
        'applications':applications,
        'application':application
    }

    return render(request, 'employer_dashboard.html', context)