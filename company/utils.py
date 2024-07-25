import re
from django.conf import settings
import os


def sanitize_db_name(name):
    """
    Sanitize the database name by replacing non-alphanumeric characters with underscores.
    """
    # Replace non-alphanumeric characters with underscores
    sanitized_name = re.sub(r'\W|^(?=\d)', '_', name)
    return sanitized_name


def get_db_path(alias):
    """
    Generate the path for the database file based on the alias.
    """
    return os.path.join('company_databases', f"{alias}.db")

def add_database_config(alias, db_name):
    """
    Add a dynamic database configuration to Django settings.
    """
    db_path = os.path.join('company_databases', f"{alias}.db")

    if alias not in settings.DATABASES:
        settings.DATABASES[alias] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': db_path,
            'ATOMIC_REQUESTS': True,
        }
        print(f"Added database configuration for '{alias}' with path '{db_path}'.")
    else:
        print(f"Database configuration for '{alias}' already exists.")
