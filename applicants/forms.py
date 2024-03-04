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
            'education',
            'phone',
            'state',
            'city',
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

class ApplicantProfileFilter(forms.ModelForm):
    class Meta:
        model = ApplicantProfile
        fields = [
            'descripcion_fisicaMotora',
            'opcion_fisicaMotora',
            'afectacion_fisicaMotora',
            'adaptaciones_fisicaMotora',
            'descripcion_sensorial',
            'opcion_sensorial',
            'afectacion_sensorial',
            'adaptaciones_sensorial',
            'descripcion_intelectual',
            'opcion_intelectual',
            'independencia',
            'adaptaciones_intelectual',
            'descripcion_psiquica',
            'opcion_psiquica',
            'adaptaciones_psiquica',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Custom Fields
        for field in self.fields:
                if isinstance(self.fields[field].widget, forms.Textarea):
                    self.fields[field].widget.attrs.update({'class':'form-control', 'rows':4})
                else:
                    self.fields[field].widget.attrs.update({'class':'form-select'})