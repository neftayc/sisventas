from django.contrib import admin
from .models.Persona import Persona
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    """doctring for Persona"""
    list_display=("nombre","dni", "f_nacimiento")
    search_fields=("nombre","f_nacimiento")
    list_per_page=2

admin.site.register(Persona, PersonaAdmin)
