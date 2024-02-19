from django import forms
from .models import JobOffer
from django.core.exceptions import ValidationError

class JobOfferDataForm(forms.ModelForm):
    class Meta:
        model = JobOffer
        fields = [
            'job_title', 
            'company_name',
            'description',
            'state',
            'municipality',
            'job_type',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza el formulario según tus necesidades, si es necesario.

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
