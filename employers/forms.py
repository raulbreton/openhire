from django import forms
from .models import EmployerProfile

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = [
            'company_name', 
            'state', 
            'municipality', 
            'postal_code', 
            'neighborhood', 
            'street_address', 
            'exterior_number', 
            'interior_number'
        ]

    def __init__(self, *args, **kwargs):
        super(EmployerProfileForm, self).__init__(*args, **kwargs)
        # Puedes personalizar los widgets, etiquetas, etc., si es necesario

        #Labels
        self.fields['company_name'].label = 'Nombre de la Compañia'
        self.fields['state'].label = 'Estado'
        self.fields['municipality'].label = 'Municipio'
        self.fields['postal_code'].label = 'Codigo Postal'
        self.fields['neighborhood'].label = 'Colonia'
        self.fields['street_address'].label = 'Calle'
        self.fields['exterior_number'].label = 'Numero Exterior'
        self.fields['interior_number'].label = 'Numero Interior'