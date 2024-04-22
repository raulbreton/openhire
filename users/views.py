#USERS VIEW.PY
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import CustomUser

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

            request.session['email'] = request.POST['email']
            request.session['password1'] = request.POST['password1']

            # Redirect to register_account_type
            return redirect('register_account_type')
        else:
            # If the form is not valid, render the registration form again with validation errors
            #messages.error(request, 'Correo electrónico o contraseña incorrectos. Por favor, inténtalo de nuevo.')
            return render(request, "register.html", {'form': form})

    # Render the registration form (GET request or after successful submission)
    return render(request, "register.html", {'form': form})

def register_account_type(request):
    email = request.session.get('email')
    password = request.session.get('password1')

    if request.method == 'POST':
        account_type = request.POST.get('account_type')

        if account_type == 'applicant':
            # Ingresar Datos al Formulario
            form_data = {
                'email': email,
                'password1': password,
                'password2': password,
                'is_applicant': True,
                'is_employer': False,
            }
            
            form = SignUpForm(form_data)
            #Guardar los datos del formulario.
            if form.is_valid(): 
                form.save()
            
             # Authenticate the user based on the provided credentials
            user = authenticate(username=email, password=password)
            
            # Log in the user
            login(request, user)

            # Use filter to get the ApplicantProfile based on the email
            pk = CustomUser.objects.filter(email=email).values('id')[0]['id']
            
            # Complementar la URL de redireccionamiento con el 'profile_id'
            redirect_url = f'/applicant-profile/{pk}/'
            return redirect(redirect_url)
        
        elif account_type == 'employer':
            # Ingresar Datos al Formulario
            form_data = {
                'email': email,
                'password1': password,
                'password2': password,
                'is_applicant': False,
                'is_employer': True,
            }
            
            form = SignUpForm(form_data)
            #Guardar los datos del formulario.
            if form.is_valid(): 
                form.save()
            
             # Authenticate the user based on the provided credentials
            user = authenticate(username=email, password=password)
            
            # Log in the user
            login(request, user)
                
            # Use filter to get the ApplicantProfile based on the email
            pk = CustomUser.objects.filter(email=email).values('id')[0]['id']
            
            # Complementar la URL de redireccionamiento con el 'profile_id'
            redirect_url = f'/employer-profile/{pk}/'
            return redirect(redirect_url)

    return render(request, "register_account_type.html")

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
            return render(request, "login.html", {})

    # If the request method is not POST, render the login.html template
    return render(request, "login.html", {})