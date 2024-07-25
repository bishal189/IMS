from django.db import models
from django.conf import settings
import os
# myapp/signals.py
import os
import subprocess
from django.db import connections, connection
from django.dispatch import receiver
from django.db.models.signals import post_save
# from .models import Company
from .utils import sanitize_db_name
from django.core.management import call_command




class Company(models.Model):
    COMPANY_TYPES = (
        ('public', 'Public'),
        ('private', 'Private'),
        # Add other types as needed
    )

    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    # User=models.ForeignKey(User,on_delete=models.CASCADE ,null=True,blank=True)
    contact_no = models.CharField(max_length=15)
    country = models.CharField(max_length=100,blank=True,null=True)
    province = models.CharField(max_length=100,blank=True,null=True)
    pan_no = models.CharField(max_length=20)
    company_type = models.CharField(max_length=20,blank=True,null=True)
    mobile_no = models.CharField(max_length=15)
    financial_year = models.CharField(max_length=9,null=True,blank=True)  # Example: 2023-2024
    db_name = models.CharField(max_length=255, unique=True,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name
    





@receiver(post_save, sender=Company)
def create_database(sender, instance, created, **kwargs):
    if created:
        sanitized_name = sanitize_db_name(instance.name)
        db_name = f"{sanitized_name}.db"
        db_path = os.path.join('company_databases', db_name)

        # Create the database file if it does not exist
        if not os.path.exists(db_path):
            open(db_path, 'w').close()