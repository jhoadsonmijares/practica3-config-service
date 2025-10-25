from django.contrib import admin
from .models import Variable

@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Variable
    """
    list_display = ['name', 'value', 'environment', 'is_sensitive', 'created_at']
    list_filter = ['environment', 'is_sensitive', 'created_at']
    search_fields = ['name', 'value', 'environment__name']
    ordering = ['environment', 'name']