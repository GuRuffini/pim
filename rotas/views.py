from rotas.models import Ambiente, Rota
from rotas.serializers import AmbienteSerializer, RotaSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class AmbienteViewSet(viewsets.ModelViewSet):
    queryset = Ambiente.objects.all()
    serializer_class = AmbienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['ambiente', 'bloco', 'andar', 'ativo']
    search_fields = ['ambiente', 'bloco', 'andar']

class RotaViewSet(viewsets.ModelViewSet):
    queryset = Rota.objects.all()
    serializer_class = RotaSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['origem__ambiente', 'destino__ambiente', 'ativo']
    search_fields = ['origem__ambiente', 'destino__ambiente', 'descricao']
