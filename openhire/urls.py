from django.contrib import admin
from django.urls import path
from users.views import register_user, login_user, logout_user
from employers.views import employers_home, employer_profile
from applicants.views import applicants_home, applicant_profile, applicant_filter

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
]