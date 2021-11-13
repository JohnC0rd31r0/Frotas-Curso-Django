from rest_framework.viewsets import ModelViewSet
from core.models import Montadora
from core.serializers import MontadoraSerializer


class MontadoraViewSet(ModelViewSet):
    queryset = Montadora.objects.all()
    serializer_class = MontadoraSerializer
