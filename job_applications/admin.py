from django.contrib import admin
from .models import JobApplication

class UserAdmin(admin.ModelAdmin):
    model = JobApplication
    #Fields to display
    list_display = ['job_offer', 'candidate']

admin.site.register(JobApplication, UserAdmin)