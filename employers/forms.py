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
            'postal_code',
            'neighborhood', 
            'street_address',
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
                    
        self.fields['company_description'].widget.attrs.update({'rows':4})
        self.fields['state'].widget.attrs.update({'class':'form-select'})