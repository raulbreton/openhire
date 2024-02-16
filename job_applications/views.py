from django.shortcuts import render, redirect
from .forms import JobApplicationForm
from job_offers.models import JobOffer

def apply_for_job(request, job_offer_id):
    job_offer = JobOffer.objects.get(pk=job_offer_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the application to the database
            application = form.save(commit=False)
            application.candidate = request.user.applicantprofile
            application.job_offer = job_offer
            application.save()
            # Redirect to the home page
            return redirect('applicants-home')
    else:
        form = JobApplicationForm()

    return render(request, 'job_applications-form-template.html', {'form': form, 'job_offer': job_offer})