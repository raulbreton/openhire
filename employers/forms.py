from django import forms
from .models import EmployerProfile

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = [
            'company_name', 
            'industry',
            'phone',
            'company_description',
            'state', 
            'city',
            'municipality', 
            'postal_code', 
            'neighborhood', 
            'street_address', 
            'exterior_number', 
            'interior_number'
        ]

    def __init__(self, *args, **kwargs):
        super(EmployerProfileForm, self).__init__(*args, **kwargs)
        #Custom Fields
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class':'form-control'})

                if field == 'company_name' or field == 'industry' or field == 'state' or field == 'city'or field == 'phone':
                    self.fields[field].required = True
                else:
                    self.fields[field].required = False

        #Hard-Coded Labels
        self.fields['company_name'].label = 'Nombre de la Compañia *'
        self.fields['company_description'].label = 'Descripción de la Compañia'
        self.fields['industry'].label = 'Industria de la Compañia*'
        self.fields['phone'].label = 'Teléfono *'
        self.fields['company_description'].help_text = '<div style="border-top: 1px solid black; margin-top: 50px;"><h3 style="margin-top: 30px;">Ubicación</h3><p style="color: rgb(134, 133, 133);">Esto permite mostrarte ofertas de empleo cercanas a tu ubicación.</p>'
        self.fields['state'].label = 'Estado *'
        self.fields['city'].label = 'Ciudad *'
        self.fields['municipality'].label = 'Municipio'
        self.fields['postal_code'].label = 'Codigo Postal'
        self.fields['neighborhood'].label = 'Colonia'
        self.fields['street_address'].label = 'Calle'
        self.fields['exterior_number'].label = 'Num. Exterior'
        self.fields['interior_number'].label = 'Num. Interior'