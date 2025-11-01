from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import (
    Tree, Post, CustomUser, Laudo, Notificacao, HistoricoNotificacao,
    EcosystemServiceConfig, EcosystemServiceHistory
)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'aprovacao_status', 'is_staff']
    list_filter = ['user_type', 'aprovacao_status', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Informações de Nível', {'fields': ('user_type', 'aprovacao_status', 'aprovado_por', 'data_aprovacao')}),
        ('Dados Técnicos', {'fields': ('formacao', 'registro_profissional', 'documento_comprobatorio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações de Nível', {'fields': ('user_type',)}),
    )


class LaudoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tree', 'autor', 'status', 'data_criacao']
    list_filter = ['status', 'data_criacao']
    search_fields = ['titulo', 'tree__nome_popular', 'autor__username']
    readonly_fields = ['data_criacao', 'data_validacao']


class HistoricoInline(admin.TabularInline):
    model = HistoricoNotificacao
    extra = 0
    readonly_fields = ['usuario', 'acao', 'observacao', 'data']
    can_delete = False


class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'autor', 'tree', 'status', 'tecnico_responsavel', 'data_criacao']
    list_filter = ['tipo', 'status', 'data_criacao']
    search_fields = ['titulo', 'descricao', 'tree__nome_popular', 'autor__username']
    readonly_fields = ['data_criacao', 'data_atualizacao']
    inlines = [HistoricoInline]


class TreeResource(resources.ModelResource):
    class Meta:
        model = Tree
        import_id_fields = ("N_placa",)
        fields = ["N_placa", "nome_popular", "nome_cientifico", "dap", "altura", "latitude", "longitude", "laudo"]


class MedicamentoDataAdmin(ImportExportModelAdmin):
    resource_class = TreeResource


# ============ ADMIN PARA SERVIÇOS ECOSSISTÊMICOS ============

class EcosystemServiceHistoryInline(admin.TabularInline):
    """Inline para exibir histórico de configurações"""
    model = EcosystemServiceHistory
    extra = 0
    readonly_fields = ['usuario', 'acao', 'valores_anteriores', 'valores_novos', 'observacao', 'data']
    can_delete = False
    can_add = False
    
    def has_change_permission(self, request, obj=None):
        return False


@admin.register(EcosystemServiceConfig)
class EcosystemServiceConfigAdmin(admin.ModelAdmin):
    """Admin customizado para configuração de serviços ecossistêmicos"""
    list_display = ['nome', 'codigo', 'categoria', 'ativo', 'valor_monetario_unitario', 'data_atualizacao']
    list_filter = ['ativo', 'categoria', 'data_atualizacao']
    search_fields = ['nome', 'codigo', 'descricao']
    readonly_fields = ['data_criacao', 'data_atualizacao', 'criado_por']
    inlines = [EcosystemServiceHistoryInline]
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'codigo', 'descricao', 'categoria', 'ativo', 'ordem_exibicao'),
            'description': 'Configure o nome, código único e informações básicas do serviço.'
        }),
        ('Cálculo', {
            'fields': ('formula', 'coeficientes'),
            'description': 'Fórmula Python que será avaliada. Use variáveis: dap, altura, biomassa, tree. Exemplo: "math.exp(coeficientes[\'BETA0\'] + coeficientes[\'BETA1\'] * math.log(dap) + coeficientes[\'BETA2\'] * math.log(altura)) / 1000"'
        }),
        ('Valoração', {
            'fields': ('valor_monetario_unitario', 'unidade_medida'),
            'description': 'Valor monetário por unidade do serviço.'
        }),
        ('Referência', {
            'fields': ('referencia_cientifica',),
            'description': 'Referência bibliográfica do modelo utilizado.'
        }),
        ('Metadados', {
            'fields': ('criado_por', 'data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        """Registra quem criou/atualizou e salva histórico"""
        if not change:  # Novo objeto
            obj.criado_por = request.user
            acao = 'Serviço criado'
        else:  # Atualização
            acao = 'Serviço atualizado'
            # Captura valores anteriores
            try:
                obj_antigo = EcosystemServiceConfig.objects.get(pk=obj.pk)
                valores_anteriores = {
                    'formula': obj_antigo.formula,
                    'coeficientes': obj_antigo.coeficientes,
                    'valor_monetario_unitario': obj_antigo.valor_monetario_unitario,
                    'ativo': obj_antigo.ativo,
                }
                valores_novos = {
                    'formula': obj.formula,
                    'coeficientes': obj.coeficientes,
                    'valor_monetario_unitario': obj.valor_monetario_unitario,
                    'ativo': obj.ativo,
                }
                
                # Cria histórico apenas se houver mudanças significativas
                if valores_anteriores != valores_novos:
                    EcosystemServiceHistory.objects.create(
                        servico=obj,
                        usuario=request.user,
                        acao=acao,
                        valores_anteriores=valores_anteriores,
                        valores_novos=valores_novos,
                        observacao=f"Atualização via admin por {request.user.username}"
                    )
            except EcosystemServiceConfig.DoesNotExist:
                pass
        
        super().save_model(request, obj, form, change)
        
        if not change:
            messages.success(request, f'Serviço "{obj.nome}" criado com sucesso!')
        else:
            messages.success(request, f'Serviço "{obj.nome}" atualizado com sucesso!')
    
    def get_queryset(self, request):
        """Limita acesso apenas a gestores ou superusers"""
        qs = super().get_queryset(request)
        if not (request.user.is_gestor() or request.user.is_superuser):
            return qs.none()
        return qs
    
    def has_add_permission(self, request):
        return request.user.is_gestor() or request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_gestor() or request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_gestor() or request.user.is_superuser


@admin.register(EcosystemServiceHistory)
class EcosystemServiceHistoryAdmin(admin.ModelAdmin):
    """Admin para histórico (somente leitura)"""
    list_display = ['servico', 'acao', 'usuario', 'data']
    list_filter = ['servico', 'data']
    search_fields = ['servico__nome', 'usuario__username', 'acao']
    readonly_fields = ['servico', 'usuario', 'acao', 'valores_anteriores', 'valores_novos', 'observacao', 'data']
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False


# ============ REGISTROS PADRÃO ============

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Tree, MedicamentoDataAdmin)
admin.site.register(Post)
admin.site.register(Laudo, LaudoAdmin)
admin.site.register(Notificacao, NotificacaoAdmin)