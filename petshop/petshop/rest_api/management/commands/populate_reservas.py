from typing import Any
from django.core.management.base import BaseCommand
from model_bakery import baker
from reserva.models import reserva


class Command(BaseCommand):
    help = 'criar dados fake para testar a api de agendamento'
    def handle(self, *args, **options):
        total = 50
        self.stdout.write(
            self.style.WARNING(f'criando {total} agendamentos')
        )
        for i in range(total):
            Reserva = baker.make(reserva)
            Reserva.save()
        self.stdout.write(
            self.style.SUCCESS('agendamentos criados')
        )

