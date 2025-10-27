import math
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.
BETA0 = -0.906586
BETA1 = 1.60421
BETA2 = 0.37162

PRECIPITATION = 1329  # Precipitação anual em São José dos Campos (L / m^2)
DIAMETER_RATIO = 4  # Razão média entre diâmetro da copa e diâmetro do tronco

RADIATION = 1661 # Radiação solar anual em São José dos Campos (kWh / m^2)
ENERGY_RATIO = 0.25 # Taxa de aproveitamento da energia das sombras


class CustomUser(AbstractUser):
    """Modelo de usuário customizado com 3 níveis de acesso"""
    
    class UserType(models.TextChoices):
        GESTOR = 'GESTOR', 'Gestor do Sistema (Nível 1)'
        TECNICO = 'TECNICO', 'Técnico Voluntário (Nível 2)'
        CIDADAO = 'CIDADAO', 'Cidadão (Nível 3)'
    
    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.CIDADAO,
        verbose_name="Tipo de Usuário"
    )
    
    # Campos específicos para Técnicos (Nível 2)
    formacao = models.CharField(max_length=255, blank=True, verbose_name="Formação")
    registro_profissional = models.CharField(max_length=100, blank=True, verbose_name="Registro Profissional")
    documento_comprobatorio = models.FileField(
        upload_to='credenciais/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        verbose_name="Documento Comprobatório"
    )
    
    class ApprovalStatus(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        APROVADO = 'APROVADO', 'Aprovado'
        REJEITADO = 'REJEITADO', 'Rejeitado'
    
    aprovacao_status = models.CharField(
        max_length=10,
        choices=ApprovalStatus.choices,
        default=ApprovalStatus.PENDENTE,
        verbose_name="Status de Aprovação"
    )
    aprovado_por = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tecnicos_aprovados',
        verbose_name="Aprovado por"
    )
    data_aprovacao = models.DateTimeField(null=True, blank=True, verbose_name="Data de Aprovação")
    
    def is_gestor(self):
        return self.user_type == self.UserType.GESTOR
    
    def is_tecnico(self):
        return self.user_type == self.UserType.TECNICO and self.aprovacao_status == self.ApprovalStatus.APROVADO
    
    def is_cidadao(self):
        return self.user_type == self.UserType.CIDADAO
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


class Tree(models.Model):
    N_placa = models.FloatField(default=0)
    nome_popular = models.CharField(max_length=255)
    nome_cientifico = models.CharField(max_length=255)
    dap = models.IntegerField()
    altura = models.FloatField()
    # data_da_coleta = models.DateField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    laudo = models.URLField(max_length=255, blank=True)
    imagem = models.URLField(max_length=255, blank=True)
    plantado_por = models.CharField(max_length=100, default="DCTA")
    species = models.ForeignKey('Species', null=True, on_delete=models.SET_NULL)

    @property
    def stored_co2(self) -> float:
        if self.dap <= 0 or self.altura <= 0:
            return 0

        return round(
            (
                math.exp(
                    BETA0 + BETA1 * math.log(self.dap) + BETA2 * math.log(self.altura)
                )
                / 1000
            ),
            4,
        )

    @property
    def stormwater_intercepted(self) -> float:
        if self.dap <= 0:
            return 0

        return math.pi * ((self.dap * DIAMETER_RATIO) / (2 * 100)) ** 2 * PRECIPITATION

    @property
    def conserved_energy(self) -> float:
        if self.dap <= 0:
            return 0

        return math.pi * ((self.dap * DIAMETER_RATIO) / (2 * 100)) ** 2 * RADIATION * ENERGY_RATIO

    @property
    def biodiversity(self) -> float:
        return self.species.bio_index if self.species is not None else 1


class Post(models.Model):
    tree = models.ForeignKey(Tree, related_name="posts", on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    specialized = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_on",)


class Species(models.Model):
    name = models.TextField()
    bio_index = models.FloatField()


class Laudo(models.Model):
    """Modelo para laudos técnicos"""
    
    class LaudoStatus(models.TextChoices):
        RASCUNHO = 'RASCUNHO', 'Rascunho'
        PENDENTE = 'PENDENTE', 'Pendente de Aprovação'
        APROVADO = 'APROVADO', 'Aprovado'
        REJEITADO = 'REJEITADO', 'Rejeitado'
    
    tree = models.ForeignKey('Tree', on_delete=models.CASCADE, related_name='laudos_tecnicos')
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='laudos_criados')
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    arquivo = models.FileField(
        upload_to='laudos/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        verbose_name="Arquivo PDF do Laudo"
    )
    status = models.CharField(
        max_length=10,
        choices=LaudoStatus.choices,
        default=LaudoStatus.RASCUNHO
    )
    validado_por = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='laudos_validados'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_validacao = models.DateTimeField(null=True, blank=True)
    observacoes_validacao = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Laudo Técnico'
        verbose_name_plural = 'Laudos Técnicos'
    
    def __str__(self):
        return f"{self.titulo} - {self.tree.nome_popular}"


class Notificacao(models.Model):
    """Modelo para notificações/denúncias de cidadãos"""
    
    class TipoNotificacao(models.TextChoices):
        DENUNCIA = 'DENUNCIA', 'Denúncia'
        EVENTO = 'EVENTO', 'Evento'
    
    class StatusNotificacao(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        EM_ANALISE = 'EM_ANALISE', 'Em Análise'
        RESOLVIDA = 'RESOLVIDA', 'Resolvida'
        ARQUIVADA = 'ARQUIVADA', 'Arquivada'
    
    tree = models.ForeignKey('Tree', on_delete=models.CASCADE, related_name='notificacoes')
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notificacoes_criadas')
    tipo = models.CharField(max_length=10, choices=TipoNotificacao.choices)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='notificacoes/', blank=True, null=True)
    status = models.CharField(
        max_length=15,
        choices=StatusNotificacao.choices,
        default=StatusNotificacao.PENDENTE
    )
    tecnico_responsavel = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notificacoes_analisadas',
        limit_choices_to={'user_type': 'TECNICO'}
    )
    parecer_tecnico = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.titulo}"


class HistoricoNotificacao(models.Model):
    """Histórico de mudanças em notificações"""
    notificacao = models.ForeignKey(Notificacao, on_delete=models.CASCADE, related_name='historico')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    acao = models.CharField(max_length=255)
    observacao = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data']
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'
