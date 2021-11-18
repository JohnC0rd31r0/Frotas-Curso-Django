from django.db.models import fields
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import Categoria, Motorista, Montadora, Veiculo, Acompanhamento


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class MotoristaSerializer(ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'


class MontadoraSerializer(ModelSerializer):
    class Meta:
        model = Montadora
        fields = '__all__'


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"


class VeiculoDetailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    montadora = MontadoraSerializer()
    motorista = SerializerMethodField()

    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1

    def get_motorista(self, instance):
        nomes_motoristas = []
        motorista = instance.motorista.get_queryset()
        for motor in motorista:
            nomes_motoristas.append(motor.nome)
        return nomes_motoristas


class AcompanhamentoSerializer(ModelSerializer):
    status = SerializerMethodField()

    class Meta:
        model = Acompanhamento
        fields = ("id", "item", "quantidade", "veiculo", "status")

    def get_status(self, instance):
        return instance.get_status_display()
