from django.contrib import admin
from .models import *


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass


@admin.register(Teeth)
class TeethAdmin(admin.ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Treatement)
class TreatementAdmin(admin.ModelAdmin):
    pass


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    pass


@admin.register(Service_Category)
class ServiceCategoryAdmin(admin.ModelAdmin):
    pass
