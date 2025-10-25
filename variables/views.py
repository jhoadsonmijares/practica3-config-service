from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Variable
from .serializers import VariableSerializer
from environments.models import Environment

class VariableViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar variables de configuración dentro de entornos
    """
    queryset = Variable.objects.all()
    serializer_class = VariableSerializer

    def get_queryset(self):
        """
        Filtrar variables por entorno si se especifica en la URL
        """
        queryset = Variable.objects.all()
        env_name = self.kwargs.get('env_name')
        if env_name:
            environment = get_object_or_404(Environment, name=env_name)
            queryset = queryset.filter(environment=environment)
        return queryset

    def create(self, request, env_name=None):
        """
        Crear una nueva variable para un entorno específico
        Sobrescribe el método create para manejar la relación con el entorno
        """
        environment = get_object_or_404(Environment, name=env_name)
        
        # Verificar si ya existe una variable con el mismo nombre en este entorno
        existing_var = Variable.objects.filter(
            name=request.data.get('name'), 
            environment=environment
        ).first()
        
        if existing_var:
            return Response(
                {"error": "Ya existe una variable con este nombre en el entorno"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(environment=environment)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)