from django.http import JsonResponse
from .models import Evento

def listar_eventos(request):
    # Busca todos os eventos do banco de dados
    eventos = Evento.objects.all()
    
    # Estrutura a lista que será transformada em JSON
    dados = []
    for evento in eventos:
        dados.append({
            'id': evento.id,
            'titulo': evento.titulo,
            'data_evento': evento.data_evento.strftime('%Y-%m-%d'),
            'capacidade_maxima': evento.capacidade_maxima,
            'ativo': evento.ativo,
            'palestrante': {
                'id': evento.palestrante.id,
                'nome': evento.palestrante.nome,
                'instituicao': evento.palestrante.instituicao
            }
        })
        
    # Retorna a resposta HTTP com o JSON (safe=False permite passar listas)
    return JsonResponse(dados, safe=False, json_dumps_params={'ensure_ascii': False})
