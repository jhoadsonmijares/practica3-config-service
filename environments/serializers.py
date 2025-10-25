from rest_framework import serializers
from .models import Environment

class EnvironmentSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Environment
    Convierte objetos Environment a JSON y viceversa
    """
    class Meta:
        model = Environment
        fields = ['name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_name(self, value):
        """
        Validar que el nombre sea un slug válido (solo letras, números, guiones)
        """
        if not value.replace('-', '').replace('_', '').isalnum():
            raise serializers.ValidationError("El nombre debe ser un URL slug válido (solo letras, números, guiones y underscores)")
        return value