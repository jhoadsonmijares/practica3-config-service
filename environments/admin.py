from django.contrib import admin
from .models import Environment

@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Environment
    """
    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    ordering = ['name']