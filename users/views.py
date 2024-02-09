#USERS VIEW.PY
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def register_user(request):
    # Initialize an instance of the SignUpForm
    form = SignUpForm()

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        # If it is a POST request, bind the form to the data in the request
        form = SignUpForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Extract cleaned data from the form
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            is_employer = form.cleaned_data['is_employer']
            is_applicant = form.cleaned_data['is_applicant']
            
            # Check if both employer and applicant checkboxes are selected
            if is_employer and is_applicant:
                # If both are selected, render the registration form again with an error message
                return render(request, "register.html", {'form': form})

            # Save the form data and potentially perform a redirect
            form.save()

            # Authenticate the user based on the provided credentials
            user = authenticate(username=email, password=password)
            
            # Log in the user
            login(request, user)

            # Check if the user is an employer
            if is_employer:
                # Redirect to Employers Home Page
                return redirect('employers-home')
            
            # Check if the user is an applicant
            elif is_applicant:
                # Redirect to Applicants Home Page
                return redirect('applicants-home')
        else:
            # If the form is not valid, render the registration form again with validation errors
            return render(request, "register.html", {'form': form})

    # Render the registration form (GET request or after successful submission)
    return render(request, "register.html", {'form': form})

def logout_user(request):
    # Retrieve the currently logged-in user from the request
    user = request.user
    
    # Log the user out using the provided 'logout' function
    logout(request)
    
    # Check if the logged-out user is an employer
    if user.is_employer == True:
        # If the user is an employer, redirect to the employers_home page
        return redirect('employers-home')
    else:
        # If the user is not an employer (presumably an applicant), redirect to the applicants_home page
        return redirect('applicants-home')
    
def login_user(request):
    # Check if the user is already authenticated, and if so, log them out
    if request.user.is_authenticated:
        logout(request)

    # Check if the request method is POST (i.e., form submission)
    if request.method == "POST":
        # Retrieve username (email) and password from the POST data
        username = request.POST['email']
        password = request.POST['password']

        # Authenticate the user with the provided credentials
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user is not None:
            # Log in the authenticated user
            login(request, user)

            # Check if the logged-in user is an employer
            if user.is_employer == True:
                # If the user is an employer, redirect to the employers-home page
                return redirect('employers-home')
            else:
                # If the user is not an employer (presumably an applicant), redirect to the applicants-home page
                return redirect('applicants-home')
        else:
            # If authentication fails, display an error message
            messages.error(request, 'Correo electrónico o contraseña incorrectos. Por favor, inténtalo de nuevo.')

    # If the request method is not POST, render the login.html template
    return render(request, "login.html", {})