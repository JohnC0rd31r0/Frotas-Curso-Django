from rest_framework.viewsets import ModelViewSet
from core.models import Acompanhamento
from core.serializers import AcompanhamentoSerializer


class AcompanhamentoViewSet(ModelViewSet):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer
