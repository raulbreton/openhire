from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter', 'resume']

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)
        
        self.fields['cover_letter'].widget = forms.Textarea(attrs={'rows': 5})
        self.fields['cover_letter'].widget.attrs.update({'class':'form-control'})
        
        self.fields['resume'].widget.attrs['accept'] = 'application/pdf' #PDF's Only Code Line
        self.fields['resume'].required = True
        self.fields['resume'].help_text = "<p style = 'color: gray; margin-top: 0px;'>Solo se aceptan documentos en PDF</p>"
        self.fields['resume'].widget.attrs.update({'class':'form-control'})