from django.contrib import admin

from core.models import Acompanhamento, Categoria, Montadora, Motorista, Veiculo
admin.site.register(Categoria)
admin.site.register(Montadora)
admin.site.register(Motorista)
admin.site.register(Veiculo)
