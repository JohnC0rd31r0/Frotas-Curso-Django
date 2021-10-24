from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
"""from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status"""
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Montadora, Motorista

import json


def teste(request):
    return HttpResponse("Olá Mundo do Django")
# Create your views here.


@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.descricao = json_data['descricao']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['descricao'] = qs.descricao
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item Excluido com sucesso!"}
        return JsonResponse(data)


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


"""

class CategoriasList(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriaDetail(APIView):
    def get(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def put(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        categoria = get_object_or_404(Categoria.objects.all(), id=id)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
"""


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


@method_decorator(csrf_exempt, name="dispatch")
class MontadoraView(View):
    def get(self, request, id=None):
        if id:
            qs = Montadora.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['nome'] = qs.nome
            return JsonResponse(data)
        else:
            data = list(Montadora.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        nova_montadora = Montadora.objects.create(**json_data)
        data = {"id": nova_montadora.id, "nome": nova_montadora.nome}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Montadora.objects.get(id=id)
        qs.nome = json_data['nome']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['nome'] = qs.nome
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Montadora.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item Excluido com sucesso!"}
        return JsonResponse(data)


class MontadoraSerializer(ModelSerializer):
    class Meta:
        model = Montadora
        fields = '__all__'


class MontadoraViewSet(ModelViewSet):
    queryset = Montadora.objects.all()
    serializer_class = MontadoraSerializer


@method_decorator(csrf_exempt, name="dispatch")
class MotoristaView(View):
    def get(self, request, id=None):
        if id:
            qs = Motorista.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['nome'] = qs.nome
            data['cnh'] = qs.cnh
            return JsonResponse(data)
        else:
            data = list(motorista.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        novo_motorista = Motorista.objects.create(**json_data)
        data = {"id": novo_motorista.id,
                "nome": novo_motorista.nome, "cnh": novo_motorista.cnh}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Motorista.objects.get(id=id)
        qs.nome = json_data['nome']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['nome'] = qs.nome
        data['cnh'] = qs.cnh
        return JsonResponse(data)

    def delete(self, request, id):
        qs = Motorista.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item Excluido com sucesso!"}
        return JsonResponse(data)


class MotoristaSerializer(ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'


class MotoristaViewSet(ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
