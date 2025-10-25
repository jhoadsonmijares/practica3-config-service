#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Configura el módulo de settings de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configservice.settings')
    
    try:
        # Intenta importar Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Si falla la importación, muestra un error útil
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Ejecuta el comando de Django
    execute_from_command_line(sys.argv)

# Punto de entrada cuando se ejecuta el script directamente
if __name__ == '__main__':
    main()