from django.contrib import admin
from .models import Applicants, Listing
from django.contrib.auth.models import Group, User

admin.site.site_header = "MAU Online Job Application Admin"

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'surname', 'othername', 'phone', 'email']
    readonly_fields = ['firstname', 'surname', 'othername', 'phone', 'email', 'address', 'resume', 'job']

class ListingAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'category']
    
admin.site.register(Listing, ListingAdmin)
admin.site.register(Applicants, ApplicantAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)