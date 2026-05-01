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

#questão6 

def calcula_pontos_sequencia_baixa(dados):
    valores = set(dados)
    
    if {1, 2, 3, 4}.issubset(valores):
        return 15
    if {2, 3, 4, 5}.issubset(valores):
        return 15
    if {3, 4, 5, 6}.issubset(valores):
        return 15
    
    return 0

#questao7

def calcula_pontos_sequencia_alta(dados):
    valores = set(dados)
    
    if {1, 2, 3, 4, 5}.issubset(valores):
        return 30
    if {2, 3, 4, 5, 6}.issubset(valores):
        return 30
    
    return 0

#questao8

def calcula_pontos_full_house(dados):
    contagem = {}

    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    valores = contagem.values()

    if 3 in valores and 2 in valores:
        soma = 0

        for dado in dados:
            soma += dado

        return soma

    return 0

#questao9

def calcula_pontos_quadra(dados):
    contagem = {}

    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    for valor in contagem.values():
        if valor >= 4:
            soma = 0

            for dado in dados:
                soma += dado

            return soma

    return 0

#questao10

def calcula_pontos_quina(dados):
    contagem = {}

    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    for valor in contagem.values():
        if valor >= 5:
            return 50

    return 0

#questao11

def calcula_pontos_regra_avancada(dados):
    pontos = {}

    pontos["cinco_iguais"] = calcula_pontos_quina(dados)
    pontos["full_house"] = calcula_pontos_full_house(dados)
    pontos["quadra"] = calcula_pontos_quadra(dados)
    pontos["sem_combinacao"] = calcula_pontos_soma(dados)
    pontos["sequencia_alta"] = calcula_pontos_sequencia_alta(dados)
    pontos["sequencia_baixa"] = calcula_pontos_sequencia_baixa(dados)

    return pontos
