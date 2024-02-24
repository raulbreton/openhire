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
        

class JobOfferDataForm(forms.ModelForm):
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
        
    def clean(self):
        cleaned_data = super().clean()
        min_salary = cleaned_data.get('min_salary')
        max_salary = cleaned_data.get('max_salary')

        if min_salary is not None and max_salary is not None and min_salary > max_salary:
            raise forms.ValidationError("El salario mínimo no puede ser mayor que el salario máximo.")
        elif min_salary == 0 and max_salary == 0:
            raise forms.ValidationError("Porfavor ingresa una cifra.")
        elif min_salary < 0 and max_salary < 0:
            raise forms.ValidationError("La cifra no puede ser menor a cero.")

        return cleaned_data


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Custom Fields
        for field in self.fields:
            if field == 'job_type' or field == 'state':
                self.fields[field].widget.attrs.update({'class':'form-select'})
                self.fields[field].required = True
            else:
                self.fields[field].widget.attrs.update({'class':'form-control'})
                self.fields[field].required = True

        #Hard-Coded Labels
        self.fields['job_title'].label = 'Titulo del Empleo *'
        self.fields['description'].label = 'Descripción del Empleo *'
        self.fields['state'].label = 'Estado *'
        self.fields['city'].label = 'Ciudad *'
        self.fields['min_salary'].label = 'Minimo *'
        self.fields['max_salary'].label = 'Maximo *'

        self.fields['company_name'].label = ''
        self.fields['company_name'].widget = forms.TextInput(attrs={
            'style': 'display: none;',
        })

class BooleanFieldsForm(forms.ModelForm):
    class Meta:
        model = JobOffer
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
            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Custom Fields

    def clean(self):
        cleaned_data = super().clean()
        
        # Lista de todas las variables booleanas en el modelo
        all_boolean_fields = [
            cleaned_data['brazo_izquierdo'],
            cleaned_data['brazo_derecho'],
            cleaned_data['mano_izquierda'],
            cleaned_data['mano_derecha'],
            cleaned_data['pierna_izquierda'],
            cleaned_data['pierna_derecha'],
            cleaned_data['pie_izquierdo'],
            cleaned_data['pie_derecho'],
            cleaned_data['espalda'],
            cleaned_data['cuello'],
            cleaned_data['vista'],
            cleaned_data['oido'],
            cleaned_data['tacto'],
            cleaned_data['sistema_respiratorio'],
            cleaned_data['sistema_cardiovascular'],
            cleaned_data['sistema_neurologico'],
            cleaned_data['sistema_neurologico_sistema_nervioso_periferico'],
        ]

        # Verificamos si al menos una variable booleana es True en la lista completa
        if not any(all_boolean_fields):
            raise ValidationError('Debe seleccionar al menos una opción del Filtro Inclusivo en el formulario.')

        return cleaned_data
    
def display_true_fields(self):
    true_fields = []

    # Extremidades superiores
    if self.cleaned_data.get('brazo_izquierdo'):
        true_fields.append('Brazo Izquierdo')
    if self.cleaned_data.get('brazo_derecho'):
        true_fields.append('Brazo Derecho')
    if self.cleaned_data.get('mano_izquierda'):
        true_fields.append('Mano Izquierda')
    if self.cleaned_data.get('mano_derecha'):
        true_fields.append('Mano Derecha')

    # Extremidades inferiores
    if self.cleaned_data.get('pierna_izquierda'):
        true_fields.append('Pierna Izquierda')
    if self.cleaned_data.get('pierna_derecha'):
        true_fields.append('Pierna Derecha')
    if self.cleaned_data.get('pie_izquierdo'):
        true_fields.append('Pie Izquierdo')
    if self.cleaned_data.get('pie_derecho'):
        true_fields.append('Pie Derecho')

    # Columna vertebral
    if self.cleaned_data.get('espalda'):
        true_fields.append('Espalda')
    if self.cleaned_data.get('cuello'):
        true_fields.append('Cuello')

    # Sistema sensorial
    if self.cleaned_data.get('vista'):
        true_fields.append('Vista')
    if self.cleaned_data.get('oido'):
        true_fields.append('Oído')
    if self.cleaned_data.get('tacto'):
        true_fields.append('Tacto')

    # Sistemas Corporales
    if self.cleaned_data.get('sistema_respiratorio'):
        true_fields.append('Sistema Respiratorio')
    if self.cleaned_data.get('sistema_cardiovascular'):
        true_fields.append('Sistema Cardiovascular')
    if self.cleaned_data.get('sistema_neurologico'):
        true_fields.append('Sistema Neurológico')
    if self.cleaned_data.get('sistema_neurologico_sistema_nervioso_periferico'):
        true_fields.append('Sistema Neurológico - Sistema Nervioso Periférico')

    return true_fields
