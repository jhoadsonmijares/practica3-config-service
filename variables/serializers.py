from rest_framework import serializers
from .models import Variable

class VariableSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Variable
    Convierte objetos Variable a JSON y viceversa
    """
    # Campo adicional para mostrar el nombre del entorno (solo lectura)
    environment_name = serializers.CharField(source='environment.name', read_only=True)

    class Meta:
        model = Variable
        fields = [
            'name', 'value', 'description', 'environment', 
            'environment_name', 'is_sensitive', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def validate_name(self, value):
        """
        Validar que el nombre sea un slug válido
        """
        if not value.replace('-', '').replace('_', '').isalnum():
            raise serializers.ValidationError("El nombre debe ser un URL slug válido (solo letras, números, guiones y underscores)")
        return value