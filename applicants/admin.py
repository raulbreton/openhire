from django.contrib import admin
from .models import ApplicantProfile

class UserAdmin(admin.ModelAdmin):
    model = ApplicantProfile
    #Fields to display
    list_display = ['user', 'first_name', 'state', 'municipality', 'postal_code', 'neighborhood', 'street_address', 'exterior_number', 'interior_number',
                    'brazo_izquierdo', 'brazo_derecho', 'mano_izquierda', 'mano_derecha',
                    'pierna_izquierda', 'pierna_derecha', 'pie_izquierdo', 'pie_derecho',
                    'espalda', 'cuello',
                    'vista', 'oido', 'tacto',
                    'sistema_respiratorio', 'sistema_cardiovascular', 'sistema_neurologico', 'sistema_neurologico_sistema_nervioso_periferico',
                    'no_especificado']

admin.site.register(ApplicantProfile, UserAdmin)