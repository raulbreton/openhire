import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openhire.settings")
import django
django.setup()

import random
from faker import Faker
from users.models import CustomUser
from applicants.models import ApplicantProfile
from employers.models import EmployerProfile
from job_offers.models import JobOffer
from job_applications.models import JobApplication

fake = Faker()

# Create fake CustomUser instances
# Create fake CustomUser instances
for _ in range(50):
    email = fake.email()
    password = '24542'
    is_employer = random.choice([True, False])
    is_applicant = not is_employer
    user = CustomUser.objects.create_user(email=email, password=password, is_employer=is_employer, is_applicant=is_applicant)

    if ApplicantProfile.objects.filter(user=user).exists():
        applicant_profile = ApplicantProfile.objects.get(user=user)

        applicant_profile.first_name=fake.first_name()
        applicant_profile.last_names=fake.last_name()
        applicant_profile.title=fake.job()
        applicant_profile.industry=fake.job()
        applicant_profile.education=fake.random_element(['Bachelor', 'Master', 'PhD'])
        applicant_profile.phone=fake.phone_number()
        applicant_profile.state=fake.random_element([
                                                        "Aguascalientes",
                                                        "Baja California",
                                                        "Baja California Sur",
                                                        "Campeche",
                                                        "Coahuila",
                                                        "Colima",
                                                        "Chiapas",
                                                        "Chihuahua",
                                                        "Ciudad de México",
                                                        "Durango",
                                                        "Guanajuato",
                                                        "Guerrero",
                                                        "Hidalgo",
                                                        "Jalisco",
                                                        "México",
                                                        "Michoacán",
                                                        "Morelos",
                                                        "Nayarit",
                                                        "Nuevo León",
                                                        "Oaxaca",
                                                        "Puebla",
                                                        "Querétaro",
                                                        "Quintana Roo",
                                                        "San Luis Potosí",
                                                        "Sinaloa",
                                                        "Sonora",
                                                        "Tabasco",
                                                        "Tamaulipas",
                                                        "Tlaxcala",
                                                        "Veracruz",
                                                        "Yucatán",
                                                        "Zacatecas"
                                                    ])                         
        applicant_profile.city=fake.city()
        applicant_profile.opcion_fisicaMotora=random.choice(['Trastornos del Estado de Ánimo', 'Trastornos de Ansiedad', 'Trastornos de la Personalidad'])
        applicant_profile.opcion_sensorial=random.choice(['Visual', 'Manos', 'Dedos'])
        applicant_profile.opcion_intelectual=random.choice(['Memoria', 'Razonamiento Lógico', 'Habilidades Sociales', 'Habilidades Motoras', 'Aprendizaje Académico'])
        applicant_profile.opcion_psiquica=random.choice(['Trastornos del Estado de Ánimo', 'Trastornos de Ansiedad', 'Trastornos de la Personalidad'])
        
        applicant_profile.afectacion_fisicaMotora=random.choice(['Leve', 'Moderada', 'Grave'])
        applicant_profile.afectacion_sensorial=random.choice(['Leve', 'Moderada', 'Grave'])
        applicant_profile.independencia=random.choice(['Leve', 'Moderada', 'Grave'])
        
        applicant_profile.save()
    else:
        employer_profile = EmployerProfile.objects.get(user=user)
        
        employer_profile.company_name=fake.company()
        employer_profile.company_description=fake.text()
        employer_profile.phone=fake.phone_number()
        employer_profile.industry=fake.job()
        employer_profile.state=fake.state()
        employer_profile.city=fake.city()
        employer_profile.postal_code=fake.zipcode()
        employer_profile.neighborhood=fake.street_name()
        employer_profile.street_address=fake.street_address()
        employer_profile.save()

# Create fake JobOffer instances
applicants = CustomUser.objects.filter(is_applicant=True)
employers = CustomUser.objects.filter(is_employer=True)

for _ in range(25):
    employer = random.choice(employers)
    job_offer = JobOffer.objects.create(
        job_title=fake.job(),
        company_name=employer.employerprofile.company_name,
        description=fake.text(),
        job_type=random.choice(['Tiempo Completo', 'Medio Tiempo', 'Becario', 'Temporal', 'Contrato']),
        min_salary=fake.random_int(min=20000, max=80000, step=1000),
        max_salary=fake.random_int(min=80000, max=150000, step=1000),
        employer_profile=employer.employerprofile,
        state=fake.random_element([
                                    "Aguascalientes",
                                    "Baja California",
                                    "Baja California Sur",
                                    "Campeche",
                                    "Coahuila",
                                    "Colima",
                                    "Chiapas",
                                    "Chihuahua",
                                    "Ciudad de México",
                                    "Durango",
                                    "Guanajuato",
                                    "Guerrero",
                                    "Hidalgo",
                                    "Jalisco",
                                    "México",
                                    "Michoacán",
                                    "Morelos",
                                    "Nayarit",
                                    "Nuevo León",
                                    "Oaxaca",
                                    "Puebla",
                                    "Querétaro",
                                    "Quintana Roo",
                                    "San Luis Potosí",
                                    "Sinaloa",
                                    "Sonora",
                                    "Tabasco",
                                    "Tamaulipas",
                                    "Tlaxcala",
                                    "Veracruz",
                                    "Yucatán",
                                    "Zacatecas"
                                ]),
        city=fake.city(),
        opcion_fisicaMotora=random.choice(['Brazos', 'Manos', 'Dedos', 'Piernas', 'Pies', 'Columna Vertebral', 'Tronco']),
        opcion_sensorial=random.choice(['Visual', 'Manos', 'Dedos']),
        opcion_intelectual=random.choice(['Memoria', 'Razonamiento Lógico', 'Habilidades Sociales', 'Habilidades Motoras', 'Aprendizaje Académico']),
        opcion_psiquica=random.choice(['Trastornos del Estado de Ánimo', 'Trastornos de Ansiedad', 'Trastornos de la Personalidad'])
    )

# Create fake JobApplication instances
for _ in range(100):
    # Get random applicant and job offer
    applicant = random.choice(applicants)
    job_offer = random.choice(JobOffer.objects.all())

    # Retrieve or create ApplicantProfile for the applicant
    applicant_profile = applicant.applicantprofile
    if not applicant_profile:
        # Create an ApplicantProfile if it doesn't exist
        applicant_profile = ApplicantProfile.objects.create(
            user=applicant,
            first_name=fake.first_name(),
            last_names=fake.last_name(),
            title=fake.job(),
            industry=fake.job(),
            education=fake.random_element(elements=('Bachelor', 'Master', 'PhD')),
            phone=fake.phone_number(),
            state=fake.state(),
            city=fake.city(),
            opcion_fisicaMotora=random.choice(['Brazos', 'Manos', 'Dedos', 'Piernas', 'Pies', 'Columna Vertebral', 'Tronco']),
            opcion_sensorial=random.choice(['Visual', 'Manos', 'Dedos']),
            opcion_intelectual=random.choice(['Memoria', 'Razonamiento Lógico', 'Habilidades Sociales', 'Habilidades Motoras', 'Aprendizaje Académico']),
            opcion_psiquica=random.choice(['Trastornos del Estado de Ánimo', 'Trastornos de Ansiedad', 'Trastornos de la Personalidad'])
        )

    # Check if a JobApplication already exists for this applicant and job offer
    existing_application = JobApplication.objects.filter(candidate=applicant_profile, job_offer=job_offer).exists()
    if not existing_application:
        JobApplication.objects.create(
            candidate=applicant_profile,
            job_offer=job_offer,
            recent_job_title=fake.job(),
            recent_job_company=fake.company(),
            fecha_inicio=fake.date_between(start_date='-1y', end_date='today'),
            fecha_fin=fake.date_between(start_date='-1y', end_date='today'),
            cover_letter=fake.text(max_nb_chars=200),
            status=random.choice(['Interesado', 'En Revisión', 'No Interesado'])
        )


