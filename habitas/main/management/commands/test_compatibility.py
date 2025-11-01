"""
Comando Django para testar compatibilidade entre cálculos antigos e novos.

Uso:
    python manage.py test_compatibility
"""

from django.core.management.base import BaseCommand
from main.models import Tree, EcosystemServiceConfig


class Command(BaseCommand):
    help = 'Testa compatibilidade entre métodos antigos (@property) e novos (BD dinâmico)'

    def handle(self, *args, **options):
        """Executa o teste de compatibilidade"""
        
        # Pega uma árvore qualquer
        tree = Tree.objects.first()
        if not tree:
            self.stdout.write(
                self.style.ERROR('❌ Nenhuma árvore encontrada para teste')
            )
            return
        
        self.stdout.write(f'Testando com árvore ID {tree.id}: {tree.nome_popular}')
        
        # Verifica se os serviços existem
        if not EcosystemServiceConfig.objects.exists():
            self.stdout.write(
                self.style.WARNING('⚠️  Nenhum serviço configurado. Execute: python manage.py init_ecosystem_services')
            )
            return
        
        # Valores antigos (métodos diretos)
        co2_antigo = tree.stored_co2
        chuva_antiga = tree.stormwater_intercepted
        energia_antiga = tree.conserved_energy
        bio_antiga = tree.biodiversity
        
        # Valores novos (via BD)
        try:
            co2_novo = tree.get_ecosystem_service_value('co2_armazenado')
        except Exception as e:
            co2_novo = None
            self.stdout.write(self.style.WARNING(f'Erro ao calcular CO₂: {e}'))
        
        try:
            chuva_nova = tree.get_ecosystem_service_value('chuva_interceptada')
        except Exception as e:
            chuva_nova = None
            self.stdout.write(self.style.WARNING(f'Erro ao calcular chuva: {e}'))
        
        try:
            energia_nova = tree.get_ecosystem_service_value('energia_conservada')
        except Exception as e:
            energia_nova = None
            self.stdout.write(self.style.WARNING(f'Erro ao calcular energia: {e}'))
        
        try:
            bio_nova = tree.get_ecosystem_service_value('biodiversidade')
        except Exception as e:
            bio_nova = None
            self.stdout.write(self.style.WARNING(f'Erro ao calcular biodiversidade: {e}'))
        
        # Compara
        tolerancia = 0.0001
        erros = []
        
        if co2_novo is not None:
            if abs(co2_antigo - co2_novo) > tolerancia:
                erros.append(f"CO₂: {co2_antigo} vs {co2_novo} (diferença: {abs(co2_antigo - co2_novo)})")
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ CO₂: {co2_antigo} = {co2_novo}')
                )
        else:
            erros.append("CO₂: Não foi possível calcular valor novo")
        
        if chuva_nova is not None:
            if abs(chuva_antiga - chuva_nova) > tolerancia:
                erros.append(f"Chuva: {chuva_antiga} vs {chuva_nova} (diferença: {abs(chuva_antiga - chuva_nova)})")
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Chuva: {chuva_antiga} = {chuva_nova}')
                )
        else:
            erros.append("Chuva: Não foi possível calcular valor novo")
        
        if energia_nova is not None:
            if abs(energia_antiga - energia_nova) > tolerancia:
                erros.append(f"Energia: {energia_antiga} vs {energia_nova} (diferença: {abs(energia_antiga - energia_nova)})")
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Energia: {energia_antiga} = {energia_nova}')
                )
        else:
            erros.append("Energia: Não foi possível calcular valor novo")
        
        if bio_nova is not None:
            if abs(bio_antiga - bio_nova) > tolerancia:
                erros.append(f"Biodiversidade: {bio_antiga} vs {bio_nova} (diferença: {abs(bio_antiga - bio_nova)})")
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Biodiversidade: {bio_antiga} = {bio_nova}')
                )
        else:
            erros.append("Biodiversidade: Não foi possível calcular valor novo")
        
        if erros:
            self.stdout.write(
                self.style.ERROR('\n❌ ERROS DE COMPATIBILIDADE:')
            )
            for erro in erros:
                self.stdout.write(self.style.ERROR(f'  - {erro}'))
        else:
            self.stdout.write(
                self.style.SUCCESS('\n✅ Compatibilidade verificada! Valores idênticos.')
            )

