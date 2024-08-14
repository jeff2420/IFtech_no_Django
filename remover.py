import os
import django

# Define as configurações do Django para o script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetoIFTECH.settings')
django.setup()

from AppPortaria.models import Veiculo

# Seu código aqui...
from django.db.models import Count

# Encontra todas as placas duplicadas
placas_duplicadas = Veiculo.objects.values('placa').annotate(placa_count=Count('placa')).filter(placa_count__gt=1)

for item in placas_duplicadas:
    placa = item['placa']
    # Pega todos os registros com a placa duplicada
    duplicatas = Veiculo.objects.filter(placa=placa)
    # Mantém apenas o primeiro registro e exclui os demais
    duplicatas.exclude(id=duplicatas.first().id).delete()