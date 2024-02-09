#APPLICANTS MODEL
from django.db import models
from users.models import CustomUser
from django.dispatch import receiver
from django.db.models.signals import post_save

class ApplicantProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #Personal Data
    first_name = models.CharField(max_length=100, default='None')

    #Address Fields
    state = models.CharField(max_length=255, default='None')
    municipality = models.CharField(max_length=255, default='None')
    postal_code = models.CharField(max_length=10, default='None')
    neighborhood = models.CharField(max_length=100, default='None')
    street_address = models.CharField(max_length=255, default='None')
    exterior_number = models.CharField(max_length=10, default='None')
    interior_number = models.CharField(max_length=10, blank=True, null=True, default='None')

    # Extremidades superiores
    brazo_izquierdo = models.BooleanField(default=False)
    brazo_derecho = models.BooleanField(default=False)  
    mano_izquierda = models.BooleanField(default=False) 
    mano_derecha = models.BooleanField(default=False)   

    # Extremidades inferiores
    pierna_izquierda = models.BooleanField(default=False)
    pierna_derecha = models.BooleanField(default=False)  
    pie_izquierdo = models.BooleanField(default=False)   
    pie_derecho = models.BooleanField(default=False)

    # Columna vertebral
    espalda = models.BooleanField(default=False)
    cuello = models.BooleanField(default=False) 

    # Sistema sensorial
    vista = models.BooleanField(default=False)
    oido = models.BooleanField(default=False) 
    tacto = models.BooleanField(default=False)

    # Sistemas Corporales
    sistema_respiratorio = models.BooleanField(default=False)
    sistema_cardiovascular = models.BooleanField(default=False)
    sistema_neurologico = models.BooleanField(default=False)
    sistema_neurologico_sistema_nervioso_periferico = models.BooleanField(default=False)

    # No especificado
    no_especificado = models.CharField(max_length=255, default="None")

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=CustomUser)
def created_profile(sender, instance, created, **kwargs):
    # Check if a new instance of CustomUser has been created
    if created and instance.is_applicant:
        # If the new user is an applicant, create a corresponding ApplicantsProfile
        ApplicantProfile.objects.create(user=instance)

# Connect the 'created_profile' function to the 'post_save' signal of 'CustomUser'
post_save.connect(created_profile, sender=CustomUser)