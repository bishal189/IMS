# Generated by Django 5.0.7 on 2024-07-24 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_customuser_company'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customUser',
        ),
    ]
