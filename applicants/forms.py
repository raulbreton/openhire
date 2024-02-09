from django import forms
from .models import ApplicantProfile

class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = [
            'first_name', 
            'state', 
            'municipality', 
            'postal_code', 
            'neighborhood', 
            'street_address', 
            'exterior_number', 
            'interior_number'
        ]

    def __init__(self, *args, **kwargs):
        super(ApplicantProfileForm, self).__init__(*args, **kwargs)
        # Puedes personalizar los widgets, etiquetas, etc., si es necesario

        #Labels
        self.fields['first_name'].label = 'Nombre'
        self.fields['state'].label = 'Estado'
        self.fields['municipality'].label = 'Municipio'
        self.fields['postal_code'].label = 'Codigo Postal'
        self.fields['neighborhood'].label = 'Colonia'
        self.fields['street_address'].label = 'Calle'
        self.fields['exterior_number'].label = 'Numero Exterior'
        self.fields['interior_number'].label = 'Numero Interior'

from django import forms
from .models import ApplicantProfile

class ApplicantFilterForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = [
            'brazo_izquierdo',
            'brazo_derecho',
            'mano_izquierda',
            'mano_derecha',
            'pierna_izquierda',
            'pierna_derecha',
            'pie_izquierdo',
            'pie_derecho',
            'espalda',
            'cuello',
            'vista',
            'oido',
            'tacto',
            'sistema_respiratorio',
            'sistema_cardiovascular',
            'sistema_neurologico',
            'sistema_neurologico_sistema_nervioso_periferico',
            'no_especificado',
        ]

    def __init__(self, *args, **kwargs):
        super(ApplicantFilterForm, self).__init__(*args, **kwargs)
        # Puedes personalizar los widgets, etiquetas, etc., si es necesario

