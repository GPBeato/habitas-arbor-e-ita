"""
Comando Django para popular serviços ecossistêmicos iniciais.

Uso:
    python manage.py init_ecosystem_services
"""

from django.core.management.base import BaseCommand
from main.models import EcosystemServiceConfig, CustomUser


class Command(BaseCommand):
    help = 'Popula os serviços ecossistêmicos iniciais do sistema'

    def handle(self, *args, **options):
        """Executa a população dos serviços"""
        
        # Tenta encontrar um gestor ou cria um superuser temporário
        gestor = CustomUser.objects.filter(user_type='GESTOR').first()
        if not gestor:
            gestor = CustomUser.objects.filter(is_superuser=True).first()
        
        if not gestor:
            self.stdout.write(
                self.style.WARNING('⚠️  Nenhum gestor encontrado. Criando serviços sem criador.')
            )
        
        servicos = [
            {
                'nome': 'Armazenamento de CO₂',
                'codigo': 'co2_armazenado',
                'descricao': 'Carbono armazenado na biomassa da árvore (Schumacher & Hall, 1933)',
                'formula': 'math.exp(coeficientes["BETA0"] + coeficientes["BETA1"] * math.log(dap) + coeficientes["BETA2"] * math.log(altura)) / 1000',
                'coeficientes': {
                    'BETA0': -0.906586,
                    'BETA1': 1.60421,
                    'BETA2': 0.37162,
                },
                'valor_monetario_unitario': 365.0,  # R$/ton/ano
                'unidade_medida': 'ton CO₂',
                'categoria': 'SEQUESTRO',
                'referencia_cientifica': 'Schumacher, F. X., & Hall, F. C. (1933). Logarithmic expression of timber-tree volume. Journal of Agricultural Research, 47(9), 719-734.',
                'ordem_exibicao': 1,
                'ativo': True,
            },
            {
                'nome': 'Interceptação de Água Pluvial',
                'codigo': 'chuva_interceptada',
                'descricao': 'Volume anual de água interceptada pela copa (Gash, 1979)',
                'formula': 'math.pi * ((dap * coeficientes["DIAMETER_RATIO"]) / (2 * 100)) ** 2 * coeficientes["PRECIPITATION"]',
                'coeficientes': {
                    'DIAMETER_RATIO': 4,
                    'PRECIPITATION': 1329,  # L/m²/ano em SJC
                },
                'valor_monetario_unitario': 0.015,  # R$/L
                'unidade_medida': 'L/ano',
                'categoria': 'INTERCEPTACAO',
                'referencia_cientifica': 'Gash, J. H. C. (1979). An analytical model of rainfall interception by forests. Quarterly Journal of the Royal Meteorological Society, 105(443), 43-55.',
                'ordem_exibicao': 2,
                'ativo': True,
            },
            {
                'nome': 'Conservação de Energia',
                'codigo': 'energia_conservada',
                'descricao': 'Energia conservada por sombreamento (Ko, 2018)',
                'formula': 'math.pi * ((dap * coeficientes["DIAMETER_RATIO"]) / (2 * 100)) ** 2 * coeficientes["RADIATION"] * coeficientes["ENERGY_RATIO"]',
                'coeficientes': {
                    'DIAMETER_RATIO': 4,
                    'RADIATION': 1661,  # kWh/m²/ano em SJC
                    'ENERGY_RATIO': 0.25,
                },
                'valor_monetario_unitario': 0.82,  # R$/kWh
                'unidade_medida': 'kWh/ano',
                'categoria': 'ENERGIA',
                'referencia_cientifica': 'Ko, Y. (2018). Trees and vegetation for residential energy conservation: A critical review for evidence-based urban greening in North America. Urban Forestry & Urban Greening, 34, 318-335.',
                'ordem_exibicao': 3,
                'ativo': True,
            },
            {
                'nome': 'Índice de Biodiversidade',
                'codigo': 'biodiversidade',
                'descricao': 'Contribuição à biodiversidade local (baseado em espécie)',
                # Verifica se tree.species existe e tem bio_index, senão retorna 1.0
                'formula': 'tree.species.bio_index if (tree.species is not None and hasattr(tree.species, "bio_index")) else 1.0',
                'coeficientes': {},
                'valor_monetario_unitario': 0,  # Sem valoração monetária padrão
                'unidade_medida': 'índice',
                'categoria': 'OUTROS',
                'referencia_cientifica': 'Estimativa própria baseada em diversidade de espécies, potencial de abrigo para fauna, produção de frutos/flores e contribuição ao ecossistema local',
                'ordem_exibicao': 4,
                'ativo': True,
            },
            {
                'nome': 'Remoção de PM2.5',
                'codigo': 'poluentes_pm25',
                'descricao': 'Remoção anual de partículas PM2.5 (baseado em i-Tree simplificado)',
                'formula': '0.0001 * biomassa * coeficientes["TAXA_REMOCAO_PM25"] * coeficientes["CONCENTRACAO_PM25"]',
                'coeficientes': {
                    'TAXA_REMOCAO_PM25': 0.05,  # g/m² de área foliar/ano
                    'CONCENTRACAO_PM25': 20.0,  # µg/m³ média SJC (estimado)
                },
                'valor_monetario_unitario': 0.50,  # R$/g (estimado)
                'unidade_medida': 'g/ano',
                'categoria': 'POLUICAO',
                'referencia_cientifica': 'i-Tree Eco v6.0. US Forest Service. Simplified model for PM2.5 removal.',
                'ordem_exibicao': 5,
                'ativo': True,
            },
            {
                'nome': 'Remoção de O₃',
                'codigo': 'poluentes_o3',
                'descricao': 'Remoção anual de ozônio (baseado em i-Tree simplificado)',
                'formula': '0.0001 * biomassa * coeficientes["TAXA_REMOCAO_O3"] * coeficientes["CONCENTRACAO_O3"]',
                'coeficientes': {
                    'TAXA_REMOCAO_O3': 0.03,  # g/m²/ano
                    'CONCENTRACAO_O3': 100.0,  # µg/m³ média SJC (estimado)
                },
                'valor_monetario_unitario': 0.45,  # R$/g (estimado)
                'unidade_medida': 'g/ano',
                'categoria': 'POLUICAO',
                'referencia_cientifica': 'i-Tree Eco v6.0. US Forest Service. Simplified model for O₃ removal.',
                'ordem_exibicao': 6,
                'ativo': True,
            },
            {
                'nome': 'Absorção Anual de Carbono',
                'codigo': 'co2_absorvido_anual',
                'descricao': 'Sequestro anual de CO₂ (diferente de armazenamento total)',
                'formula': 'biomassa * coeficientes["TAXA_CRESCIMENTO_ANUAL"] * 0.5',  # 0.5 = proporção C na biomassa
                'coeficientes': {
                    'TAXA_CRESCIMENTO_ANUAL': 0.02,  # 2% ao ano (taxa fixa simplificada)
                },
                'valor_monetario_unitario': 365.0,  # R$/ton/ano
                'unidade_medida': 'ton CO₂/ano',
                'categoria': 'SEQUESTRO',
                'referencia_cientifica': 'Modelo simplificado baseado em taxas de crescimento anual médio. Adaptado de Nowak et al. (2013).',
                'ordem_exibicao': 7,
                'ativo': True,
            },
        ]
        
        criados = 0
        atualizados = 0
        
        for dados in servicos:
            servico, created = EcosystemServiceConfig.objects.update_or_create(
                codigo=dados['codigo'],
                defaults={
                    **dados,
                    'criado_por': gestor,
                }
            )
            if created:
                criados += 1
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Criado: {servico.nome}')
                )
            else:
                atualizados += 1
                self.stdout.write(
                    self.style.WARNING(f'↻ Atualizado: {servico.nome}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Total: {criados} criados, {atualizados} atualizados'
            )
        )

