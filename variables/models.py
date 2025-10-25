from django.db import models
from django.utils import timezone
from environments.models import Environment

class Variable(models.Model):
    """
    Modelo para representar una variable de configuración dentro de un entorno
    """
    name = models.SlugField(
        max_length=100,
        help_text="Nombre único de la variable en un entorno. Debe ser un URL slug."
    )
    value = models.TextField(
        help_text="Valor de la variable."
    )
    description = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        help_text="Breve explicación de para qué sirve la variable."
    )
    environment = models.ForeignKey(
        Environment, 
        on_delete=models.CASCADE,
        related_name='variables',
        help_text="Entorno al que pertenece esta variable"
    )
    is_sensitive = models.BooleanField(
        default=False,
        help_text="Indica si es sensible (e.g., True para contraseñas)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación de la variable"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha de última actualización de la variable"
    )

    class Meta:
        db_table = 'variables'
        unique_together = ['name', 'environment']  # Nombre único por entorno
        ordering = ['name']

    def __str__(self):
        return f"{self.environment.name}.{self.name}"