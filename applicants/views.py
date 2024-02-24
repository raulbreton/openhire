from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ApplicantProfile
from users.models import CustomUser
from .forms import ApplicantProfileForm, ApplicantFilterForm
from job_offers.models import JobOffer

def applicants_home(request):
    return render( request, "applicants-home.html")

@login_required  # restrict access to authenticated users
def applicant_profile(request, pk):
    # Retrieve the ApplicantProfile instance based on the provided primary key (pk)
    applicant_profile = ApplicantProfile.objects.get(user_id=pk)

    if request.method == 'POST':
        # If the form is submitted, update the instance with the posted data
        form = ApplicantProfileForm(request.POST, instance=applicant_profile)
        if form.is_valid():
            form.save()
            #Succes!
            return redirect('applicant-filter', pk=pk)
    else:
        # If it's a GET request, display the form with the existing data
        form = ApplicantProfileForm(instance=applicant_profile)

    context = {
        'form': form,
        'applicant_profile': applicant_profile,
    }

    return render(request, 'applicant-profile.html', context)

@login_required  # restrict access to authenticated users
def applicant_filter(request, pk):
    # Retrieve the ApplicantProfile instance based on the provided primary key (pk)
    applicant_profile = ApplicantProfile.objects.get(user_id=pk)

    if request.method == 'POST':
        # If the form is submitted, update the instance with the posted data
        filter_form = ApplicantFilterForm(request.POST, instance=applicant_profile)
        if filter_form.is_valid():
            filter_form.save()
            #Succes!
            return redirect('applicant-filter', pk=pk)
    else:
        # If it's a GET request, display the form with the existing data
        filter_form = ApplicantFilterForm(instance=applicant_profile)

    context = {
        'filter_form': filter_form,
        'applicant_profile': applicant_profile,
    }

    return render(request, 'applicant-filter.html', context)

def search_job_offers(request):
    job_title_query = request.GET.get('job_title', '')
    job_offers = JobOffer.objects.filter(job_title__icontains=job_title_query)

    if not job_offers:
        return render(request, 'no_results.html', {'job_title_query': job_title_query})
    
    return render(request, 'search_results.html', {'job_offers': job_offers})