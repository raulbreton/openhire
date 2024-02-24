from django.shortcuts import render,redirect
from .forms import JobOfferDataForm, BooleanFieldsForm, JobOfferForm
from .models import JobOffer
from employers.models import EmployerProfile

def job_offer_data_view(request):
    if not request.user.is_authenticated or not request.user.is_applicant:
        return redirect('login')  # Redirect to login if the user is not an employer
    
    if request.method == 'POST':
        form = JobOfferDataForm(request.POST)
        
        if form.is_valid():
            job_offer_data = form.save(commit=False)

            # Convert Decimal to float before saving to session to avoid 'Object of type Decimal is not JSON serializable' Error
            job_offer_data.min_salary = float(job_offer_data.min_salary)
            job_offer_data.max_salary = float(job_offer_data.max_salary)
            
            # Store data in the session
            request.session['job_offer_data'] = { 
                'job_title': job_offer_data.job_title,
                'company_name': job_offer_data.company_name,
                'description': job_offer_data.description,
                'state': job_offer_data.state,
                'city': job_offer_data.city,
                'job_type': job_offer_data.job_type,
                'min_salary': job_offer_data.min_salary,
                'max_salary': job_offer_data.max_salary,
            }
            
            return redirect('job_offer-inclusive-fields') # Redirect to the inclusive filter template after succesful submissions
    else:
        form = JobOfferDataForm()
        company_name = EmployerProfile.objects.get(user=request.user).company_name  # Retrieve company name from employer's profile
        state = EmployerProfile.objects.get(user=request.user).state  # Retrieve company name from employer's profile
        city = EmployerProfile.objects.get(user=request.user).city  # Retrieve company name from employer's profile
        initial_data = {'company_name': company_name, 'state': state, 'city': city}
        form = JobOfferDataForm(initial=initial_data)

    return render(request, 'job_offer_data_form.html', {'form': form})

def select_boolean_fields(request):
    if request.method == 'POST':
        form = BooleanFieldsForm(request.POST)
        employer_profile = EmployerProfile.objects.get(user=request.user)
        if form.is_valid():
            boolean_fields = form.save(commit=False)

            # Retrieve job_offer_data from session
            job_offer_data_session = request.session.get('job_offer_data', {})

            # Combine the dictionaries
            job_offer = JobOffer(**job_offer_data_session,**form.cleaned_data)
            job_offer.employer_profile = employer_profile
            job_offer.save()
            return redirect('employers-home')
    else:
        form = BooleanFieldsForm()

    return render(request, 'job_offer_boolean_fields_form.html', {'form': form})