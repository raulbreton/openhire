from django.contrib import admin
from .models import ApplicantProfile

class UserAdmin(admin.ModelAdmin):
    model = ApplicantProfile
    #Fields to display
    list_display = ['user', 'first_name']

admin.site.register(ApplicantProfile, UserAdmin)