from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'recent_job_title', 
            'recent_job_company',
            'fecha_inicio',
            'fecha_fin',
            'cover_letter', 
            'resume'
            ]

    def __init__(self, *args, **kwargs):
        super(JobApplicationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'fecha_inicio' or field == 'fecha_fin':
                self.fields[field].widget = forms.DateInput(
                    format="%Y-%m-%d",
                    attrs={
                        'class': 'form-control',
                        'type': 'date'
                    }
                )
            else:
                self.fields[field].widget.attrs.update({'class':'form-control'})
        
        self.fields['recent_job_title'].label = 'Cargo'
        self.fields['recent_job_company'].label = 'Compañia'

        self.fields['cover_letter'].label = 'Carta de Presentación'
        self.fields['cover_letter'].widget = forms.Textarea(attrs={'rows': 4})
        self.fields['cover_letter'].widget.attrs.update({'class':'form-control'})
        
        self.fields['resume'].widget.attrs['accept'] = 'application/pdf' #PDF's Only Code Line
        self.fields['resume'].required = True
        self.fields['resume'].help_text = "<p style = 'color: gray; margin-top: 0px;'>Solo se aceptan documentos en PDF</p>"
        
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        # Asegurarse de que la fecha de inicio sea anterior a la fecha de fin
        if fecha_inicio and fecha_fin and fecha_inicio >= fecha_fin:
            self.add_error('fecha_inicio', 'La fecha de inicio debe ser anterior a la fecha de fin.')

        return cleaned_data