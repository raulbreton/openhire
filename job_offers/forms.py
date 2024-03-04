from django import forms
from .models import JobOffer
from django.core.exceptions import ValidationError

class JobOfferForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = [
            'job_title', 
            'company_name',
            'description',
            'state',
            'city',
            'job_type',
            'min_salary',
            'max_salary',
            'opcion_fisicaMotora',
            'opcion_sensorial',
            'opcion_intelectual',
            'opcion_psiquica',
            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Custom Fields
        for field in self.fields:
            if self.fields[field].__class__ != forms.BooleanField:
                if field.startswith('o'):
                    self.fields[field].widget.attrs.update({'class':'form-select'})
                elif isinstance(self.fields[field].widget, forms.Textarea):
                    self.fields[field].widget.attrs.update({'class':'form-control','rows':4})
                else:
                    self.fields[field].widget.attrs.update({'class':'form-control'})
        
        self.fields['job_type'].widget.attrs.update({'class':'form-select'})
        self.fields['state'].widget.attrs.update({'class':'form-select'})
    
    def clean(self):
        cleaned_data = super().clean()

        min_salary = cleaned_data.get('min_salary')
        max_salary = cleaned_data.get('max_salary')

        # Check if min_salary is greater than or equal to max_salary
        if min_salary is not None and max_salary is not None and min_salary >= max_salary:
            raise forms.ValidationError("Minimum salary must be less than maximum salary.")

        # Check if min_salary and max_salary are non-negative
        if min_salary is not None and min_salary < 0:
            raise forms.ValidationError("Minimum salary cannot be negative.")

        if max_salary is not None and max_salary < 0:
            raise forms.ValidationError("Maximum salary cannot be negative.")
        
        opcion_fisicaMotora = cleaned_data.get('opcion_fisicaMotora')
        opcion_sensorial = cleaned_data.get('opcion_sensorial')
        opcion_intelectual = cleaned_data.get('opcion_intelectual')
        opcion_psiquica = cleaned_data.get('opcion_psiquica')

        # Check if at least one option is selected
        if not any([opcion_fisicaMotora, opcion_sensorial, opcion_intelectual, opcion_psiquica]):
            raise forms.ValidationError("Please select at least one option in either opcion_fisicaMotora, opcion_sensorial, opcion_intelectual, or opcion_psiquica.")

        return cleaned_data