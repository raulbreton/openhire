import os
import random
import django
from faker import Faker  # Asegúrate de instalar la librería faker: pip install faker
from django.core.management.base import BaseCommand


fake = Faker()

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openhire.settings')

# Configure Django and load apps
django.setup()

from users.models import CustomUser
from applicants.models import ApplicantProfile
from employers.models import EmployerProfile
from job_offers.models import JobOffer
from job_applications.models import JobApplication

class Command(BaseCommand):
    help = 'Populate data for testing purposes'

    def handle(self, *args, **options):
        # Crea usuarios
        for _ in range(10):
            email = fake.email()
            user, created = CustomUser.objects.get_or_create(email=email, is_applicant=True)

            if ApplicantProfile.objects.filter(user=user).exists():
                # Retrieve the existing ApplicantProfile
                applicant_profile = ApplicantProfile.objects.get(user=user)

                # Update all fields with new fake data
                applicant_profile.first_name = fake.first_name()
                applicant_profile.last_names = fake.last_name()
                applicant_profile.title = fake.job()
                applicant_profile.industry = fake.random_element(['Technology', 'Finance', 'Healthcare', 'Manufacturing', 'Education'])
                applicant_profile.school = fake.company()
                applicant_profile.phone = fake.phone_number()
                applicant_profile.state = fake.random_element(['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche'])
                applicant_profile.city = fake.city()
                applicant_profile.municipality = fake.city_suffix()
                applicant_profile.postal_code = fake.zipcode()
                applicant_profile.neighborhood = fake.city()
                applicant_profile.street_address = fake.street_address()
                applicant_profile.exterior_number = fake.building_number()
                applicant_profile.interior_number = fake.building_number()
                applicant_profile.brazo_izquierdo = fake.boolean()
                applicant_profile.brazo_derecho = fake.boolean()
                applicant_profile.mano_izquierda = fake.boolean()
                applicant_profile.mano_derecha = fake.boolean()
                applicant_profile.pierna_izquierda = fake.boolean()
                applicant_profile.pierna_derecha = fake.boolean()
                applicant_profile.pie_izquierdo = fake.boolean()
                applicant_profile.pie_derecho = fake.boolean()
                applicant_profile.espalda = fake.boolean()
                applicant_profile.cuello = fake.boolean()
                applicant_profile.vista = fake.boolean()
                applicant_profile.oido = fake.boolean()
                applicant_profile.tacto = fake.boolean()
                applicant_profile.sistema_respiratorio = fake.boolean()
                applicant_profile.sistema_cardiovascular = fake.boolean()
                applicant_profile.sistema_neurologico = fake.boolean()
                applicant_profile.sistema_neurologico_sistema_nervioso_periferico = fake.boolean()
                applicant_profile.no_especificado = fake.word()

                # Save the modified ApplicantProfile
                applicant_profile.save()

        for _ in range(5):
            email = fake.email()
            user, created = CustomUser.objects.get_or_create(email=email, is_employer=True)
            
            # Check if an EmployerProfile already exists for the user
            if EmployerProfile.objects.filter(user=user).exists():
                # Retrieve the existing EmployerProfile
                employer_profile = EmployerProfile.objects.get(user=user)

                # Update all fields with new fake data
                employer_profile.company_name = fake.company()
                employer_profile.company_description = fake.text()
                employer_profile.phone = fake.phone_number()
                employer_profile.industry = fake.random_element(['Technology', 'Finance', 'Healthcare', 'Manufacturing', 'Education'])
                employer_profile.state = fake.state()
                employer_profile.city = fake.city()
                employer_profile.municipality = fake.city_suffix()
                employer_profile.postal_code = fake.zipcode()
                employer_profile.neighborhood = fake.city()
                employer_profile.street_address = fake.street_address()
                employer_profile.exterior_number = fake.building_number()
                employer_profile.interior_number = fake.building_number()

                # Save the modified EmployerProfile
                employer_profile.save()    

        # Crea ofertas de trabajo
        for _ in range(10):
            employer = EmployerProfile.objects.order_by('?').first()
            job_offer = JobOffer.objects.create(
                job_title=fake.job(),
                company_name=employer.company_name,
                description=fake.text(),
                job_type=random.choice(['Tiempo Completo', 'Medio Tiempo', 'Becario', 'Temporal', 'Contrato']),
                min_salary=random.randint(20000, 50000),
                max_salary=random.randint(50001, 80000),
                employer_profile=employer,
                state=random.choice(['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche']),
                city=fake.city(),
                brazo_izquierdo=random.choice([True, False]),
                brazo_derecho=random.choice([True, False]),
                mano_izquierda=random.choice([True, False]),
                mano_derecha=random.choice([True, False]),
                pierna_izquierda=random.choice([True, False]),
                pierna_derecha=random.choice([True, False]),
                pie_izquierdo=random.choice([True, False]),
                pie_derecho=random.choice([True, False]),
                espalda=random.choice([True, False]),
                cuello=random.choice([True, False]),
                vista=random.choice([True, False]),
                oido=random.choice([True, False]),
                tacto=random.choice([True, False]),
                sistema_respiratorio=random.choice([True, False]),
                sistema_cardiovascular=random.choice([True, False]),
                sistema_neurologico=random.choice([True, False]),
                sistema_neurologico_sistema_nervioso_periferico=random.choice([True, False]),
            )

            for _ in range(10):
                candidate = ApplicantProfile.objects.order_by('?').first()
                job_offer = JobOffer.objects.order_by('?').first()

                # Check if a JobApplication already exists for the combination
                job_application, created = JobApplication.objects.get_or_create(
                candidate=candidate,
                job_offer=job_offer,
                defaults={
                    'recent_job_title': fake.job(),
                    'recent_job_company': fake.company(),
                    'fecha_inicio': fake.date_this_decade(),
                    'fecha_fin': fake.date_this_decade(),
                    'cover_letter': fake.text(),
                    'resume': 'path/to/resume.pdf',
                    'status': fake.random_element(['Enviado', 'Interesado', 'En Revisión', 'No Interesado'])
                }
                )
                

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))

if __name__ == '__main__':
    # Run the management command
    command = Command()
    command.handle()