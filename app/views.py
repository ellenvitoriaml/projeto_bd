from django.shortcuts import render
from django.http import JsonResponse
import json
import os

ARQUIVO_JSON = os.path.join(os.path.dirname(__file__), 'data/usuarios.json')

def inicializar_arquivo_json():
    if not os.path.exists(ARQUIVO_JSON) or os.path.getsize(ARQUIVO_JSON) == 0:
        with open(ARQUIVO_JSON, 'w') as file:
            json.dump([], file)

inicializar_arquivo_json()

def criar_usuario(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        nome = request.POST.get('nome')
        data_nascimento = request.POST.get('data_nascimento')

        with open(ARQUIVO_JSON, 'r') as file:
            usuarios = json.load(file)
            usuarios.append({'cpf': cpf, 'nome': nome, 'data_nascimento': data_nascimento})
        with open(ARQUIVO_JSON, 'w') as file:
            json.dump(usuarios, file)

        return JsonResponse({'message': 'Usuário cadastrado com sucesso!'})

    return render(request, 'cadastro.html')

def consulta_usuario(request):
    if request.method == 'GET':
        cpf = request.GET.get('cpf')
        nome = request.GET.get('nome')
        
        if os.path.exists(ARQUIVO_JSON) and os.path.getsize(ARQUIVO_JSON) > 0:
            with open(ARQUIVO_JSON, 'r') as file:
                usuarios = json.load(file)
                
            usuario_encontrado = None
            for usuario in usuarios:
                if cpf and usuario['cpf'] == cpf:
                    usuario_encontrado = usuario
                    break
                if nome and usuario['nome'] == nome:
                    usuario_encontrado = usuario
                    break

            if usuario_encontrado:
                return render(request, 'consulta.html', {'usuario_encontrado': usuario_encontrado})
            else:
                mensagem = 'Usuário não encontrado.'
                return render(request, 'consulta.html', {'mensagem': mensagem})
        else:
            mensagem = 'Nenhum usuário encontrado.'
            return render(request, 'consulta.html', {'mensagem': mensagem})

    return render(request, 'consulta.html')

def usuario_encontrado(request, cpf):
    with open('projeto_bd/app_bd/data/usuarios.json', 'r') as file:
        usuarios = json.load(file)
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return render(request, 'usuario_encontrado.html', {'usuario': usuario})
    
    return JsonResponse({'message': 'Usuário não encontrado.'})

def index(request):
   return render(request, 'index.html')