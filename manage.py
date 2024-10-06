#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD5a4d063d767694bd7a5f3f98fd9ead0a3dba2d04
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "archive_senegal.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "entreprise.settings")
>>>>>>> 5a4d063d767694bd7a5f3f98fd9ead0a3dba2d04
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
