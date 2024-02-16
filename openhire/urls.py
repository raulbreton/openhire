from django.contrib import admin
from django.urls import path
from users.views import register_user, login_user, logout_user
from employers.views import employers_home, employer_profile
from applicants.views import applicants_home, applicant_profile, applicant_filter, search_job_offers
from job_offers.views import job_offer_data_view, select_boolean_fields
from job_applications.views import apply_for_job

urlpatterns = [
    path('admin/', admin.site.urls),
    #USERS
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #EMPLOYERS
    path('employers-home', employers_home, name='employers-home'),
    path('employer-profile/<int:pk>', employer_profile, name="employer-profile"),
    #APPLICANTS
    path('applicants-home', applicants_home, name='applicants-home'),
    path('applicant-profile/<int:pk>/', applicant_profile, name='applicant-profile'),
    path('applicant-filter/<int:pk>/', applicant_filter, name='applicant-filter'),
    path('search/', search_job_offers, name='search_job_offers'),
    #JOB OFFER
    path('create-job_offer', job_offer_data_view, name='create-job_offer'),
    path('job_offer-inclusive-fields', select_boolean_fields, name='job_offer-inclusive-fields'),
    #JOB OFFER
    path('job/<int:job_offer_id>/apply/', apply_for_job, name='apply_for_job'),
]