#APPLICANTS MODEL
from django.db import models
from users.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save
    
class ApplicantProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False)
    last_names = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=255, null=True)
    industry = models.CharField(max_length=255, null=True)
    education = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
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
    state = models.CharField(max_length=255, choices=STATE_CHOICES, null=False, default='Aguascalientes')
    city = models.CharField(max_length=255, null=False)

    #FILTRO INCLUSIVO
    
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
        return self.user.email

@receiver(post_save, sender=CustomUser)
def created_profile(sender, instance, created, **kwargs):
    # Check if a new instance of CustomUser has been created
    if created and instance.is_applicant:
        # If the new user is an applicant, create a corresponding ApplicantsProfile
        profile = ApplicantProfile.objects.create(user=instance)

# Connect the 'created_profile' function to the 'post_save' signal of 'CustomUser'
post_save.connect(created_profile, sender=CustomUser)