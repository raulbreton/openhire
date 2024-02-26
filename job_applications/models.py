from django.db import models
from applicants.models import ApplicantProfile
from job_offers.models import JobOffer

class JobApplication(models.Model):
    candidate = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    application_date = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Enviado', 'Enviado'),
        ('Interesado', 'Interesado'),
        ('En Revisión', 'En Revisión'),
        ('No Interesado', 'No Interesado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Enviado')

    def __str__(self):
        return f"{self.candidate.user.email} - {self.job_offer.job_title}"