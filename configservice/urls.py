from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from environments.views import EnvironmentViewSet, status_check
from variables.views import VariableViewSet

# Configurar el router para las vistas ViewSet
# El router automáticamente crea las URLs para list, create, retrieve, update, destroy
router = DefaultRouter()
router.register(r'environments', EnvironmentViewSet, basename='environment')
router.register(r'environments/(?P<env_name>[^/.]+)/variables', VariableViewSet, basename='variable')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/', status_check, name='status-check'),
    path('api/', include(router.urls)),
    
    # Endpoint adicional para el JSON de consumo masivo
    path('api/environments/<str:env_name>.json', 
         EnvironmentViewSet.as_view({'get': 'json'}), 
         name='environment-json'),
]