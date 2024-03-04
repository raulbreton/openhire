from django.db import models
from applicants.models import ApplicantProfile
from job_offers.models import JobOffer

class JobApplication(models.Model):
    candidate = models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    recent_job_title = models.CharField(max_length=100, null=True)
    recent_job_company = models.CharField(max_length=255, null=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    application_date = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Interesado', 'Interesado'),
        ('En Revisión', 'En Revisión'),
        ('No Interesado', 'No Interesado'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='En Revisión')

    class Meta:
        unique_together = ('candidate', 'job_offer')

    def __str__(self):
        return f"{self.candidate.user.email} - {self.job_offer.job_title}"