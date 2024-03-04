from django.db import models
from employers.models import EmployerProfile

class JobOffer(models.Model):
    JOB_TYPE_CHOICES = (
        ('Tiempo Completo', 'Tiempo Completo'),
        ('Medio Tiempo', 'Medio Tiempo'),
        ('Becario', 'Becario'),
        ('Temporal', 'Temporal'),
        ('Contrato', 'Contrato'),
    )
    STATE_CHOICES = (
        ('Aguascalientes', 'Aguascalientes'),
        ('Baja California', 'Baja California'),
        ('Baja California Sur', 'Baja California Sur'),
        ('Campeche', 'Campeche'),
        ('Chiapas', 'Chiapas'),
        ('Chihuahua', 'Chihuahua'),
        ('Coahuila', 'Coahuila'),
        ('Colima', 'Colima'),
        ('Durango', 'Durango'),
        ('Guanajuato', 'Guanajuato'),
        ('Guerrero', 'Guerrero'),
        ('Hidalgo', 'Hidalgo'),
        ('Jalisco', 'Jalisco'),
        ('México', 'México'),
        ('Michoacán', 'Michoacán'),
        ('Morelos', 'Morelos'),
        ('Nayarit', 'Nayarit'),
        ('Nuevo León', 'Nuevo León'),
        ('Oaxaca', 'Oaxaca'),
        ('Puebla', 'Puebla'),
        ('Querétaro', 'Querétaro'),
        ('Quintana Roo', 'Quintana Roo'),
        ('San Luis Potosí', 'San Luis Potosí'),
        ('Sinaloa', 'Sinaloa'),
        ('Sonora', 'Sonora'),
        ('Tabasco', 'Tabasco'),
        ('Tamaulipas', 'Tamaulipas'),
        ('Tlaxcala', 'Tlaxcala'),
        ('Veracruz', 'Veracruz'),
        ('Yucatán', 'Yucatán'),
        ('Zacatecas', 'Zacatecas'),
    )

    #Job Offer Data
    job_title = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, null=True, default='Tiempo Completo')
    created_at = models.DateTimeField(auto_now_add=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    max_salary = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    employer_profile = models.ForeignKey(
        EmployerProfile, on_delete=models.CASCADE, 
        related_name='job_offers', # Nombre que se utilizará para acceder a las ofertas de trabajo desde un objeto EmployerProfile.
        default=None
    )

    #CONDICIONES FISICAS
    #Address Fields
    state = models.CharField(max_length=255, choices=STATE_CHOICES, null=True, default='Aguascalientes')
    city = models.CharField(max_length=255, null=True)

    # Discapacidad Física o Motora:
    PHYSICAL_CHOICES = (
        ('Brazos', 'Brazos'),
        ('Manos ', 'Manos '),
        ('Dedos', 'Dedos'),
        ('Piernas', 'Piernas'),
        ('Pies', 'Pies'),
        ('Columna Vertebral', 'Columna Vertebral'),
        ('Tronco', 'Tronco'),
    )

    AFECTACION_CHOICES = (
        ('Leve', 'Leve'),
        ('Moderada', 'Moderada'),
        ('Grave', 'Grave'),
    )

    descripcion_fisicaMotora = models.TextField(max_length=250, blank=True)  
    opcion_fisicaMotora = models.CharField(blank=True, choices=PHYSICAL_CHOICES)
    afectacion_fisicaMotora = models.CharField(blank=True, choices=AFECTACION_CHOICES)  
    adaptaciones_fisicaMotora = models.TextField(max_length=250, blank=True)  

    #Discapacidad Sensorial
    SENSOR_CHOICES = (
        ('Visual', 'Visual'),
        ('Manos ', 'Manos '),
        ('Dedos', 'Dedos'),
    )

    descripcion_sensorial = models.TextField(max_length=250, blank=True)  
    opcion_sensorial = models.CharField(blank=True, choices=SENSOR_CHOICES)
    afectacion_sensorial = models.CharField(blank=True, choices=AFECTACION_CHOICES)  
    adaptaciones_sensorial = models.TextField(max_length=250, blank=True) 

    #Discapacidad Intelectual
    INTELECTUAL_CHOICES = (
        ('Memoria', 'Memoria'),
        ('Razonamiento Lógico', 'Razonamiento Lógico'),
        ('Habilidades Sociales', 'Habilidades Sociales'),
        ('Habilidades Motoras', 'Habilidades Motoras'),
        ('Aprendizaje Académico', 'Aprendizaje Académico'),
    )
    
    descripcion_intelectual = models.TextField(max_length=250, blank=True)  
    opcion_intelectual = models.CharField(blank=True, choices=INTELECTUAL_CHOICES)
    independencia = models.CharField(blank=True, choices=AFECTACION_CHOICES)  
    adaptaciones_intelectual = models.TextField(max_length=250, blank=True)

    #Discapacidad Psiquica
    PHSYCH_CHOICES = (
        ('Trastornos del Estado de Ánimo', 'Trastornos del Estado de Ánimo'),
        ('Trastornos de Ansiedad', 'Trastornos de Ansiedad'),
        ('Trastornos de la Personalidad', 'Trastornos de la Personalidad'),
    )
    
    descripcion_psiquica = models.TextField(max_length=250, blank=True)  
    opcion_psiquica = models.CharField(blank=True, choices=PHSYCH_CHOICES)
    adaptaciones_psiquica = models.TextField(max_length=250, blank=True) 

    def __str__(self):
        return(
            f"{self.job_title}"
            f"{self.company_name}"
            #f"({self.created_at:%d-%m-%Y})"
        )