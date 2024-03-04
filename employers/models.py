from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import CustomUser

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #Personal Data
    company_name = models.CharField(max_length=100, null=True)
    company_description = models.TextField(null=True)
    phone = models.CharField(max_length=100, null=True)
    industry = models.CharField(max_length=255, null=True)

    #Address Fields
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
    city = models.CharField(max_length=255, null=True)
    postal_code = models.CharField(max_length=10, null=True)
    neighborhood = models.CharField(max_length=100, null=True)
    street_address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=CustomUser)
def created_profile(sender, instance, created, **kwargs):
    # Check if a new instance of CustomUser has been created
    if created and instance.is_employer:
        # If the new user is an applicant, create a corresponding ApplicantsProfile
        EmployerProfile.objects.create(user=instance)

# Connect the 'created_profile' function to the 'post_save' signal of 'CustomUser'
post_save.connect(created_profile, sender=CustomUser)