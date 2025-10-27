from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Tree, Post, CustomUser, Laudo, Notificacao, HistoricoNotificacao


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


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Tree, MedicamentoDataAdmin)
admin.site.register(Post)
admin.site.register(Laudo, LaudoAdmin)
admin.site.register(Notificacao, NotificacaoAdmin)