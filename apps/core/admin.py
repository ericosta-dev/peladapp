from django.contrib import admin
from apps.core.models import Configuracoes,Goleiro,Jogador

# Register your models here.
class ConfiguracoesAdmin(admin.ModelAdmin):
    pass

class GoleiroAdmin(admin.ModelAdmin):
    pass
class JogadorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Configuracoes, ConfiguracoesAdmin)
admin.site.register(Goleiro, GoleiroAdmin)
admin.site.register(Jogador, JogadorAdmin)
