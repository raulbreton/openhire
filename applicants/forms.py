from django import forms
from .models import ApplicantProfile

class ApplicantProfileForm(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = [
            'first_name',
            'last_names',
            'title',
            'industry',
            'school',
            'phone',
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
        super(ApplicantProfileForm, self).__init__(*args, **kwargs)

        #Custom Fields
        for field in self.fields:
                if field != 'state':
                    self.fields[field].widget.attrs.update({'class':'form-control'})
                else:
                    self.fields[field].widget.attrs.update({'class':'form-select'})

                if field == 'first_name' or field == 'last_names' or field == 'state' or field == 'city':
                    self.fields[field].required = True
                else:
                    self.fields[field].required = False

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

        """for field in self.fields:
            if field != 'no especificado':
                self.fields[field].widget.attrs.update({'class':'onoffswitch','id': 'myonoffswitch'})"""
        
        mixed_load = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'onoffswitch','id': 'myonoffswitch'}))

        self.fields['no_especificado'].widget.attrs['class'] = 'form-control'