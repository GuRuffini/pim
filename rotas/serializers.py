from rest_framework import serializers
from rotas.models import Ambiente, Rota

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = ['id', 'ambiente', 'bloco', 'andar', 'adicionado', 'ativo']

class RotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rota
        fields = ['id', 'origem', 'destino', 'descricao', 'adicionado', 'ativo']
