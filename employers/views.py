from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EmployerProfile
from .forms import EmployerProfileForm

def employers_home(request):
    return render( request, "employers-home.html")

@login_required  # restrict access to authenticated users
def employer_profile(request, pk):
    # Retrieve the ApplicantProfile instance based on the provided primary key (pk)
    employer_profile = EmployerProfile.objects.get(user_id=pk)

    if request.method == 'POST':
        # If the form is submitted, update the instance with the posted data
        form = EmployerProfileForm(request.POST, instance=employer_profile)
        if form.is_valid():
            form.save()
            #Succes!
            return redirect('employer-profile', pk=pk)
    else:
        # If it's a GET request, display the form with the existing data
        form = EmployerProfileForm(instance=employer_profile)

    context = {
        'form': form,
        'employer': employer_profile,
    }

    return render(request, 'employer-profile.html', context)