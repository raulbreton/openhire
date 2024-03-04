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
            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Custom Fields
        for field in self.fields:
            if self.fields[field].__class__ != forms.BooleanField:
                if field == 'state' or field == 'job_type':
                    self.fields[field].widget.attrs.update({'class':'form-select'})
                else:
                    self.fields[field].widget.attrs.update({'class':'form-control'})