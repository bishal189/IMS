from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Apply migrations to the custom database'

    def handle(self, *args, **kwargs):
        from django.core.management import call_command
        call_command('migrate', database='company_bishal')
        self.stdout.write(self.style.SUCCESS('Migrations applied to custom database successfully.'))
