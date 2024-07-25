# models.py

from django.db import models

class Todo(models.Model):
    part_name = models.CharField(max_length=255 , null=True)
    contact = models.CharField(max_length=20 , null=True)
    email = models.EmailField(max_length=50 , null=True)
    address = models.TextField(max_length=50 , null=True)
    website = models.URLField(max_length=50 , null=True)
    designation = models.CharField(max_length=100 , null=True)
    task = models.TextField(max_length=50 , null=True)
    priority = models.IntegerField(default=1, help_text="Priority on a scale of 1 to 10" , null=True)
    handled_by = models.CharField(max_length=255 , null=True)
    status = models.CharField(max_length=20,  null=True ,  choices=[
        ('New', 'New'),
        ('Qualified', 'Qualified'),
        ('On Progress', 'On Progress'),
        ('Done', 'Done'),
        ('Decline', 'Decline'),
    ])

   
