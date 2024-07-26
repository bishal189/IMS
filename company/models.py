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

    




