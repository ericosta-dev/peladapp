from django.contrib import admin
from apps.core.models import Configuracoes

# Register your models here.
class ConfiguracoesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Configuracoes, ConfiguracoesAdmin)