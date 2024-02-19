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

    #Job Offer Data
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    min_salary = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    max_salary = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    employer_profile = models.ForeignKey(
        EmployerProfile, on_delete=models.CASCADE, 
        related_name='job_offers', # Nombre que se utilizará para acceder a las ofertas de trabajo desde un objeto EmployerProfile.
        default=None
    )

    #CONDICIONES FISICAS
    #Address Fields
    state = models.CharField(max_length=255, default='None')
    municipality = models.CharField(max_length=255, default='None')

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

    def __str__(self):
        return(
            f"{self.job_title}"
            f"{self.company_name}"
            #f"({self.created_at:%d-%m-%Y})"
        )