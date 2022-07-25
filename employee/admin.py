from django.contrib import admin
from django.apps import apps
from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ['rut', 'firstname', 'lastname', 'address', 
    'phone', 'gender', 'companyDate', 'perfil', 'area', 'dep', 'position']
  list_editable = ['']
  search_fields = ['rut']
  list_per_page = 5

# all other models
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass