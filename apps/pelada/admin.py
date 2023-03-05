from django.contrib import admin

from apps.pelada.models import Pelada,PresencaGoleiro,PresencaJogador

# Register your models here.
class GoleiroInline(admin.TabularInline):
    model = PresencaGoleiro

class JogadorInline(admin.TabularInline):
    model = PresencaJogador

class PeladaAdmin(admin.ModelAdmin):
    inlines = [
        GoleiroInline,
        JogadorInline,
    ]


admin.site.register(Pelada, PeladaAdmin)