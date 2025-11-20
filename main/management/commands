from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Crée un superuser avec mot de passe'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--email', required=True)
        parser.add_argument('--password', required=True)
        parser.add_argument('--noinput', action='store_true')

    def handle(self, *args, **options):
        User = get_user_model()
        
        if not User.objects.filter(username=options['username']).exists():
            User.objects.create_superuser(
                username=options['username'],
                email=options['email'],
                password=options['password']
            )
            self.stdout.write(self.style.SUCCESS('Superuser créé avec succès!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser existe déjà'))
