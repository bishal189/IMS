# Generated by Django 4.2.7 on 2023-12-06 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_todo_address_alter_todo_contact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='party_name',
            new_name='part_name',
        ),
    ]
