from django.contrib import admin
from .models import JobOffer

class UserAdmin(admin.ModelAdmin):
    model = JobOffer
    #Fields to display
    list_display = ['job_title']

admin.site.register(JobOffer, UserAdmin)