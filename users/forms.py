from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', 'is_applicant', 'is_employer')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo Electrónico'
        self.fields['email'].label = ''
        self.fields['email'].help_text = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<p class="form-text text-muted" style="margin-top: 0%;"><small>Tu contraseña debe contener al menos 8 caracteres.</small></p>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirma la Contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small></small></span>'

        self.fields['is_applicant'].label = ''
        
        self.fields['is_applicant'].widget = forms.TextInput(attrs={
            'style': 'display: none;',
        })

        self.fields['is_employer'].label = ''
        
        self.fields['is_employer'].widget = forms.TextInput(attrs={
            'style': 'display: none;',
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado. Por favor, utiliza otro correo.")
        return email