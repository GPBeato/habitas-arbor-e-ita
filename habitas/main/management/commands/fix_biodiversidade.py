"""
Comando Django para corrigir fórmula de biodiversidade no BD.

Uso:
    python manage.py fix_biodiversidade
"""

from django.core.management.base import BaseCommand
from main.models import EcosystemServiceConfig


class Command(BaseCommand):
    help = 'Corrige a fórmula de biodiversidade para incluir hasattr no contexto'

    def handle(self, *args, **options):
        """Corrige o serviço de biodiversidade"""
        
        try:
            servico = EcosystemServiceConfig.objects.get(codigo='biodiversidade')
            
            # Nova fórmula corrigida
            nova_formula = 'tree.species.bio_index if (tree.species is not None and hasattr(tree.species, "bio_index")) else 1.0'
            
            if servico.formula != nova_formula:
                servico.formula = nova_formula
                servico.save()
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Fórmula de biodiversidade corrigida!')
                )
            else:
                self.stdout.write(
                    self.style.WARNING('Fórmula já está correta.')
                )
                
        except EcosystemServiceConfig.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('❌ Serviço de biodiversidade não encontrado. Execute: python manage.py init_ecosystem_services')
            )

