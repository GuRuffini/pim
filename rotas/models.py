from django.utils import timezone
from django.db import models

class Ambiente(models.Model):

    BLOCO = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]

    ANDAR = [
        ('T', 'Terreo'),
        ('P', 'Primeiro'),
        ('S', 'Segundo'),
    ]

    ambiente = models.CharField(max_length=255)
    bloco = models.CharField(max_length=1, choices=BLOCO, blank=False, null=False)
    andar = models.CharField(max_length=1, choices=ANDAR, blank=False, null=False)
    adicionado = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.ambiente} - Bloco {self.bloco}, Andar {self.get_andar_display()}'

class Rota(models.Model):
    origem = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='rota_origem')
    destino = models.ForeignKey(Ambiente, on_delete=models.CASCADE, related_name='rota_destino')
    descricao = models.TextField()
    adicionado = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.origem} -> {self.destino}'

    @property
    def rota(self):
        return f'{self.origem} -> {self.destino}'
