#questao1

import random

def rolar_dados(qtd):
    lista = []
    
    for i in range(qtd):
        dado = random.randint(1, 6)
        lista.append(dado)
    
    return lista

#questao2

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    del dados_rolados[dado_para_guardar]

    return [dados_rolados, dados_no_estoque]

#questao3

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado)
    del dados_no_estoque[dado_para_remover]

    return [dados_rolados, dados_no_estoque]

#questao4

def calcula_pontos_regra_simples(dados):
    pontos = {}

    for numero in range(1, 7):
        soma = 0

        for dado in dados:
            if dado == numero:
                soma += dado

        pontos[numero] = soma

    return pontos

#questao5

def calcula_pontos_soma(dados):
    soma = 0
    
    for dado in dados:
        soma += dado
    
    return soma