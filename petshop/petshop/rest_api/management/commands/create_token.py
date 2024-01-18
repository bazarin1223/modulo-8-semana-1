from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "criar um novo token para ser usado."

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        self.stdout.write(self.style.WARNING(f'Criando usuário com o nome {username}'))

        user = User.objects.create_user(username=username, password=password)
        user.first_name = username  # Definindo o primeiro nome como o nome de usuário
        user.save()

        self.stdout.write(self.style.SUCCESS('Usuário criado!'))
        self.stdout.write(self.style.WARNING('Criando token para o usuário'))

        token, created = Token.objects.get_or_create(user=user)

        self.stdout.write(self.style.SUCCESS(f'Token criado para o usuário: {token.key}'))



    
    
      
