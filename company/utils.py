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

import os
from pathlib import Path
from django.core.management import call_command
from django.conf import settings

def create_company_database(company_name):
    """
    Create a new database file for a company and apply migrations.
    """
    # Define the path for the new database
    db_path = os.path.join('company_databases', f"{company_name}.sqlite3")
    
    # Create the database directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Define a unique alias for the new database
    alias = company_name
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(BASE_DIR / f'{db_path}')

    # Add database configuration dynamically
    if alias not in settings.DATABASES:
        settings.DATABASES[alias] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / f'{db_path}',
                    'TIME_ZONE': 'Asia/Tokyo',

            'ATOMIC_REQUESTS': True,
            'CONN_HEALTH_CHECKS': False,
            'CONN_MAX_AGE': 30,
            'OPTIONS': {},
            'AUTOCOMMIT': True
        }
        print(f"Added database configuration for '{alias}' with path '{db_path}'.")

    # Create and apply migrations for the new database
    try:
        print("Creating migrations for new database...")
        call_command('makemigrations')
        print("Applying migrations...")
        call_command('migrate', database=alias)
    except Exception as e:
        print(f"Error during migration: {e}")
        raise

