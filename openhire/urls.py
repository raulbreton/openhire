from django.contrib import admin
from django.urls import path
from users.views import register_user, login_user, logout_user, register_account_type
from employers.views import employers_home, employer_profile
from applicants.views import applicants_home, applicant_profile, search_job_offers, applicant_filter, job_recommendations
from job_applications.views import apply_for_job, delete_application, set_status
from employers_dashboard.views import job_offers, job_applications, application_details, applicant_details
from applicants_dashboard.views import applicant_dashboard
from job_offers.views import create_job_offer, mod_job_offer, delete_job_offer

urlpatterns = [
    path('', login_user, name='login'),
    path('admin/', admin.site.urls),
    #USERS
    path('register/', register_user, name='register'),
    path('register_account_type/', register_account_type, name='register_account_type'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    #EMPLOYERS
    path('employers-home', employers_home, name='employers-home'),
    path('employer-profile/<int:pk>/', employer_profile, name="employer-profile"),
    #APPLICANTS
    path('applicants-home', applicants_home, name='applicants-home'),
    path('applicant-profile/<int:pk>/', applicant_profile, name='applicant-profile'),
    path('applicant-filter/<int:pk>/<str:site>/', applicant_filter, name='applicant-filter'),
    path('search/', search_job_offers, name='search_job_offers'),
    #JOB OFFER
    path('create_job_offer/', create_job_offer, name='create_job_offer'),
    path('mod_job_offer/<int:job_pk>/', mod_job_offer, name='mod_job_offer'),
    path('delete_job_offer/<int:job_pk>/', delete_job_offer, name='delete_job_offer'),
    #JOB APPLICATIONS
    path('apply_for_job/<int:job_offer_id>/', apply_for_job, name='apply_for_job'),
    path('delete_application/<int:pk>/', delete_application, name='delete_application'),
    path('set_status/<int:pk>/<str:status>/', set_status, name='set_status'),
    #EMPLOYERS DASHBOARD
    path('employers-dashboard/<int:pk>/', job_offers, name='employer-dashboard'),
    path('job_applications/<int:job_offer_id>/', job_applications, name='job_applications'),
    path('application_details/<int:application_id>/', application_details, name='application_details'),
    path('applicant_details/<int:application_id>/', applicant_details, name='applicant_details'),
    #APPLICANTS DASHBOARD
    path('applicants-dashboard/<int:pk>/', applicant_dashboard, name='applicant-dashboard'),
    ]