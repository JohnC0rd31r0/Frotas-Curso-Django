from django.contrib import admin

from core.models import Acompanhamento, Categoria, Montadora, Motorista, Veiculo, ItensEntrega
admin.site.register(Categoria)
admin.site.register(Montadora)
admin.site.register(Motorista)
admin.site.register(Veiculo)


class ItensInline(admin.TabularInline):
    model = ItensEntrega


@admin.register(Acompanhamento)
class AcompAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
