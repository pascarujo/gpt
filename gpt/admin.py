from django.contrib import admin
from .models import Instalacao, Origem, Documento

class OrigemAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome','atualizado_em','criado_em')
    search_fields = ['nome','sigla']

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()


class InstalacaoAdmin(admin.ModelAdmin):
    fields = ['sigla','nome', 'tipo', 'regional','criado_por']
    list_display = ('sigla', 'nome', 'tipo', 'regional','atualizado_em','criado_em')
    list_filter = ['regional','tipo','criado_em']
    search_fields = ['nome','sigla']

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()


class DocumentoAdmin(admin.ModelAdmin):
    fields = ['codigo','titulo','data_doc','origem','tipo','instalacoes','referencias','criado_por','arquivo']
    filter_horizontal = ['instalacoes','referencias']
    list_display = ('codigo','titulo','origem','tipo','data_doc','atualizado_em','arquivo')
    list_filter = ['origem','tipo','data_doc','instalacoes']
    search_fields = ['codigo','titulo']

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

# Register your models here.
admin.site.register(Instalacao, InstalacaoAdmin)
admin.site.register(Origem, OrigemAdmin)
admin.site.register(Documento, DocumentoAdmin)