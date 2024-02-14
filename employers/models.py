from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import CustomUser

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #Personal Data
    company_name = models.CharField(max_length=100, default='None')
    #Address Fields
    state = models.CharField(max_length=255, default='None')
    municipality = models.CharField(max_length=255, default='None')
    postal_code = models.CharField(max_length=10, default='None')
    neighborhood = models.CharField(max_length=100, default='None')
    street_address = models.CharField(max_length=255, default='None')
    exterior_number = models.CharField(max_length=10, default='None')
    interior_number = models.CharField(max_length=10, blank=True, null=True, default='None')
    
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