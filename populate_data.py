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
for _ in range(10):
    email = fake.email()
    password = fake.password()
    is_employer = random.choice([True, False])
    is_applicant = not is_employer
    user = CustomUser.objects.create_user(email=email, password=password, is_employer=is_employer, is_applicant=is_applicant)

    if is_applicant:
        # Check if ApplicantProfile already exists for this user
        if not hasattr(user, 'applicantprofile'):
            ApplicantProfile.objects.create(
                user=user,
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
    else:
        # Check if EmployerProfile already exists for this user
        if not hasattr(user, 'employerprofile'):
            EmployerProfile.objects.create(
                user=user,
                company_name=fake.company(),
                company_description=fake.text(),
                phone=fake.phone_number(),
                industry=fake.job(),
                state=fake.state(),
                city=fake.city(),
                postal_code=fake.zipcode(),
                neighborhood=fake.street_name(),
                street_address=fake.street_address()
            )

# Create fake JobOffer instances
applicants = CustomUser.objects.filter(is_applicant=True)
employers = CustomUser.objects.filter(is_employer=True)

for _ in range(5):
    employer = random.choice(employers)
    job_offer = JobOffer.objects.create(
        job_title=fake.job(),
        company_name=employer.employerprofile.company_name,
        description=fake.text(),
        job_type=random.choice(['Tiempo Completo', 'Medio Tiempo', 'Becario', 'Temporal', 'Contrato']),
        min_salary=fake.random_int(min=20000, max=80000, step=1000),
        max_salary=fake.random_int(min=80000, max=150000, step=1000),
        employer_profile=employer.employerprofile,
        state=fake.state(),
        city=fake.city(),
        opcion_fisicaMotora=random.choice(['Brazos', 'Manos', 'Dedos', 'Piernas', 'Pies', 'Columna Vertebral', 'Tronco']),
        opcion_sensorial=random.choice(['Visual', 'Manos', 'Dedos']),
        opcion_intelectual=random.choice(['Memoria', 'Razonamiento Lógico', 'Habilidades Sociales', 'Habilidades Motoras', 'Aprendizaje Académico']),
        opcion_psiquica=random.choice(['Trastornos del Estado de Ánimo', 'Trastornos de Ansiedad', 'Trastornos de la Personalidad'])
    )

    # Create fake JobApplication instances
for _ in range(20):
    candidate = random.choice(ApplicantProfile.objects.all())
    job_offer = random.choice(JobOffer.objects.all())

    # Check if a JobApplication already exists for this candidate and job offer
    existing_application = JobApplication.objects.filter(candidate=candidate, job_offer=job_offer).exists()
    if not existing_application:
        JobApplication.objects.create(
            candidate=candidate,
            job_offer=job_offer,
            recent_job_title=fake.job(),
            recent_job_company=fake.company(),
            fecha_inicio=fake.date_between(start_date='-1y', end_date='today'),
            fecha_fin=fake.date_between(start_date='-1y', end_date='today'),
            cover_letter=fake.text(max_nb_chars=200),
            status=random.choice(['Interesado', 'En Revisión', 'No Interesado'])
        )

