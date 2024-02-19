from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employers.models import EmployerProfile
from job_offers.models import JobOffer

@login_required  # restrict access to authenticated users
def employer_dashboard(request, pk):
    # Obtener todas las ofertas de trabajo del empleador actual
    employer_profile = EmployerProfile.objects.get(user_id=pk)
    job_offers = JobOffer.objects.filter(employer_profile=employer_profile)

    context = {
        'job_offers': job_offers,
    }

    return render(request, 'employer_dashboard.html', context)