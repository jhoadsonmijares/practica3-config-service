from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Environment
from .serializers import EnvironmentSerializer
from variables.models import Variable
from variables.serializers import VariableSerializer

class EnvironmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar entornos de configuración
    Proporciona automáticamente: list, create, retrieve, update, partial_update, destroy
    """
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    lookup_field = 'name'  # Usar 'name' como identificador en lugar de 'id'

    @action(detail=True, methods=['get'])
    def variables(self, request, name=None):
        """
        Endpoint personalizado: Listar variables de un entorno específico
        URL: /api/environments/{env_name}/variables/
        """
        environment = self.get_object()
        variables = Variable.objects.filter(environment=environment)
        
        # Paginación automática del REST Framework
        page = self.paginate_queryset(variables)
        if page is not None:
            serializer = VariableSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = VariableSerializer(variables, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def json(self, request, name=None):
        """
        Endpoint de consumo masivo: Devuelve todo el JSON de configuración para un entorno
        URL: /api/environments/{env_name}.json
        """
        environment = self.get_object()
        variables = Variable.objects.filter(environment=environment)
        
        # Crear diccionario plano con todas las variables
        config_dict = {}
        for variable in variables:
            # Si es sensible, no mostrar el valor real
            if variable.is_sensitive:
                config_dict[variable.name] = "***SENSITIVE***"
            else:
                config_dict[variable.name] = variable.value
        
        return Response(config_dict)

# Vista para el health check (fuera del ViewSet)
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def status_check(request):
    """
    Health Check endpoint - responde simplemente 'pong'
    URL: /status/
    """
    return Response({"status": "pong"})