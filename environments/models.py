from django.db import models
from django.utils import timezone

class Environment(models.Model):
    """
    Modelo para representar un entorno de configuración (DEV, TEST, PROD, etc.)
    """
    name = models.SlugField(
        max_length=100, 
        unique=True,
        help_text="Nombre único del entorno. Debe ser un URL slug."
    )
    description = models.TextField(
        max_length=500, 
        blank=True, 
        null=True,
        help_text="Breve explicación de para qué sirve el entorno."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha de creación del entorno"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha de última actualización del entorno"
    )

    class Meta:
        db_table = 'environments'
        ordering = ['name']

    def __str__(self):
        return self.name