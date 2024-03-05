from django.shortcuts import render,redirect
from .forms import JobOfferForm
from employers.models import EmployerProfile
from django.shortcuts import get_object_or_404
from .models import JobOffer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the trained tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("/home/raulbreton/proyecto_modular/openhire/bert/bert_classifier/checkpoint-12")
model = AutoModelForSequenceClassification.from_pretrained("/home/raulbreton/proyecto_modular/openhire/bert/bert_classifier/checkpoint-12")

def predict_label(description):
    # Tokenize the job offer description
    inputs = tokenizer(description, return_tensors="pt", truncation=True, padding=True)

    # Make the prediction
    with torch.no_grad():
        logits = model(**inputs).logits

    # Convert logits to probabilities
    probabilities = torch.softmax(logits, dim=1)

    # Get the predicted label (0 or 1)
    predicted_label = torch.argmax(probabilities, dim=1).item()

    return predicted_label

def create_job_offer(request):
    if not request.user.is_authenticated or not request.user.is_employer:
        return redirect('login')  # Redirect to login if the user is not an employer
    
    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        if form.is_valid():
            form.clean()
            form = form.save(commit=False)

            # Convert Decimal to float before saving to session to avoid 'Object of type Decimal is not JSON serializable' Error
            form.min_salary = float(form.min_salary)
            form.max_salary = float(form.max_salary)
            form.employer_profile = EmployerProfile.objects.get(user=request.user)

            # Predict the label for the job offer description
            description = form.description  # Assuming the description is a field in your form
            predicted_label = predict_label(description)
            
            if predicted_label == 1:
                form.save()
                return redirect('employers-home')  # Redirect to a success page or any desired page
            else:
                return redirect('create_job_offer')
    else:
        form = JobOfferForm()
        company_name = EmployerProfile.objects.get(user=request.user).company_name  # Retrieve company name from employer's profile
        state = EmployerProfile.objects.get(user=request.user).state  # Retrieve company name from employer's profile
        city = EmployerProfile.objects.get(user=request.user).city  # Retrieve company name from employer's profile
        initial_data = {'company_name': company_name, 'state': state, 'city': city}
        form = JobOfferForm(initial=initial_data)

    return render(request, 'job_offer.html', {'form': form})

def mod_job_offer(request, job_pk):
    if not request.user.is_authenticated or not request.user.is_employer:
        return redirect('login')  # Redirect to login if the user is not an employer
    
    job_offer_instance = get_object_or_404(JobOffer, pk=job_pk)
    form = JobOfferForm(instance=job_offer_instance)
    if request.method == 'POST':
        form = JobOfferForm(request.POST, instance=job_offer_instance)
        if form.is_valid():
            form.clean()
            form = form.save(commit=False)

            # Convert Decimal to float before saving to session to avoid 'Object of type Decimal is not JSON serializable' Error
            form.min_salary = float(form.min_salary)
            form.max_salary = float(form.max_salary)

            form.save()
            return redirect('employers-home')  # Redirect to a success page or any desired page
    else:
        form = JobOfferForm(instance=job_offer_instance)

    return render(request, 'job_offer.html', {'form': form})

def delete_job_offer(request, job_pk):
    job_offer_instance = get_object_or_404(JobOffer, id=job_pk)
    job_offer_instance.delete()
    
    return redirect('employers-home')