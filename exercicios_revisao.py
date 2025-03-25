import math

# 1. Faça uma função que receba o nome de uma pessoa como entrada e retorne uma saudação.
# Exemplo:
# Boa tarde, Samuel. Seja bem vindo!
def saudacao(nome):
    mensagem = f"Boa tarde, {nome}. Seja bem vindo!"
    return mensagem



# 2. Faça uma função que peça o raio de um círculo e retorne sua área.
def area_circulo(raio):
    area = math.pi*math.pow(raio, 2)
    return area



# 3. Faça uma função que converta a temperatura de Fahrenheit para Celsius.
# C = 5 * ((F-32) / 9).
def fahrenheit_para_celsius(farenheit):
    celsius = int(5 * ((farenheit - 32) / 9))
    return celsius



# 4. Faça uma função que calcule a multa por excesso de peso de peixes.
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça uma funçao que receba como 
# entrada o peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
# Exemplos de saidas para os parâmetros 70 e 25 respectivamente:
#
# Excesso de peso: 20 kg.
# Multa a pagar: R$ 80.00.
#
# Peso dentro do limite. Nenhuma multa aplicada.
def calculo_multa(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso*4.00
        mensagem = f"Excesso de peso: {excesso:.0f} kg.\nMulta a pagar: R$ {multa:.2f}."
        return mensagem
    else :
        excesso = 0
        mensagem = "Peso dentro do limite. Nenhuma multa aplicada."
        return mensagem



# 5. Faça uma função para calcular a quantidade de tinta necessária para pintar uma área.
# O função deverá receber o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
# galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
# os valores para cima, isto é, considere latas cheias.

## Exemplo de saída para uma área de 100 metros quadrados
# Quantidade de latas de 18L: 2
# Preço total: R$ 160.00
# 
# Quantidade de galões de 3,6L: 6
# Preço total: R$ 150.00
#
# Quantidade de latas: 1, Quantidade de galões: 1
# Preço total: R$ 105.00

def calcular_tinta():
    pass




# 6. Faça uma função que receba dois números e retorne o maior deles.
def maior_numero(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else: 
        return "Possuem o mesmo valor."



# 7. Faça uma função que verifique se uma letra é vogal ou consoante.
def verificar_letra(letra):
    if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
        return "Vogal"
    else:
        return "Consoante"



# 8. Faça um Programa que receba três números e retorne o maior deles.
def maior_tres_numeros(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        return n1
    elif (n2 > n1) and (n2 > n3):
        return n2
    elif (n3 > n1) and (n3 > n2):
        return n3



# 9. Faça uma função que retorne o menor valor entre três numeros informados.
def produto_mais_barato(n1, n2, n3):
    return min(n1,n2,n3)



# 10. Faça uma funçao que retorne uma saudação com base no turno de estudo.
# A entrada deverá ser M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
def saudacao_turno(turno):
    if (turno == "M"):
        return "Bom Dia!"
    elif (turno == "V"):
        return"Bom Tarde!"
    elif (turno == "N"):
        return "Bom Noite!"
    else:
        return "Valor Inválido!"



# 11. Faça uma função para um caixa eletrônico que informe quantas notas de cada valor serão fornecidas
# ao ser solicitado um saque.
# A função receberá como entrada o valor do saque e e retornará quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo de saída para uma entrada de 346
# Notas fornecidas:
# 3 nota(s) de R$ 100
# 4 nota(s) de R$ 10
# 1 nota(s) de R$ 5
# 1 nota(s) de R$ 1

def caixa_eletronico(saque):
    if (saque >= 10) and (saque <= 600):
        notas100 = 0
        notas50 = 0
        notas10 = 0
        notas5 = 0
        notas1 = 0
        resultado = ""
        if (saque >= 100):
            while (saque >= 100):
                saque = saque - 100
                notas100 = notas100 + 1
            resultado = f"Notas fornecidas:\n{notas100} nota(s) de R$ 100\n"
        if (saque >= 50):
            while (saque >= 50):
                saque = saque - 50
                notas50 = notas50 + 1
            resultado = resultado + f"{notas50} nota(s) de R$ 50\n"
        if (saque >= 10):
            while (saque >= 10):
                saque = saque - 10
                notas10 = notas10 + 1
            resultado = resultado + f"{notas10} nota(s) de R$ 10\n"
        if (saque >= 5):
            while (saque >= 5):
                saque = saque - 5
                notas5 = notas5 + 1
            resultado = resultado + f"{notas5} nota(s) de R$ 5\n"
        if (saque >= 1):
            while (saque >= 1):
                saque = saque - 1
                notas1 = notas1 + 1
            resultado = resultado + f"{notas1} nota(s) de R$ 1\n"

        return resultado
    else:
        return "Valor inválido."

              

# 12. Desenvolva uma lógica que classifique uma pessoa com base nas respostas sobre um crime.
# A função deverá receber receba a resposta as seguintes perguntas:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def classificar_participacao(vetor):
        if (vetor.count("sim") == 2):
            classificacao = "Suspeita"
        elif (vetor.count("sim") == 3) or (vetor.count("sim") == 4):
            classificacao = "Cúmplice"
        elif (vetor.count("sim") == 5):
            classificacao = "Assassino"
        else:
            classificacao = "Inocente"
        return classificacao

print(classificar_participacao(["sim", "sim", "não", "não", "não"]))



# 13. Faça um Programa que calcule o preço da carne em uma promoção com desconto opcional.
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
# receberá ainda um desconto de 5% sobre o total da compra. Escreva uma função que receba o tipo e a quantidade de
# carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de
# carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def calcular_preco_carne(tipo, qtd, cartao):
    desconto = 0
    if (tipo == "File Duplo"):
        if (qtd <= 5.0):
            precoTotal = 4.9*qtd
        else:
            precoTotal = 5.8*qtd
    elif (tipo == "Alcatra"):
        if (qtd <= 5.0):
            precoTotal = 5.9*qtd
        else:
            precoTotal = 6.8*qtd
    elif (tipo == "Picanha"):
        if (qtd <= 5.0):
            precoTotal = 6.9*qtd
        else:
            precoTotal = 7.8*qtd
    else:
        "Valor(es) inválido(s)"
    if (cartao == False):
        precoFinal = precoTotal
        tipoPagm = "Dinheiro"
    else:
        desconto = (5/100)*precoTotal
        precoFinal = precoTotal-desconto
        tipoPagm = "Cartão Tabajara"
    
    cupomFiscal = f"Tipo de carne: {tipo}\nQuantidade comprada: {qtd}\nPreço total: {precoTotal}\nTipo de pagamento: {cartao}\nValor do desconto: {desconto}\nValor final: {round(precoFinal,2)}"
    
    return precoFinal



# 14. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.
def potencia(base, expoente):
    resultado = base ** expoente
    return resultado



# 15. Faça um Programa que retorne o menor, maior e a soma de um conjunto de números.
def estatisticas_numeros(n):
    menor = min(n)
    maior = max(n)
    soma = sum(n)
    return (menor, maior, soma)



# 16. Faça uma função que valide se uma nota está entre 0 e 10.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
# Exemplos de saídas para as entradas -1 e 5.5 respectivamente:
# Erro: A nota deve estar entre 0 e 10. Tente novamente.
# Nota válida: 5.5
def validar_nota():
    while True:
        try:
            nota = input("Digite a nota: ")  # Pede a entrada do usuário
            nota = float(nota)  # Tenta converter a entrada para um número decimal (float)
            
            if 0 <= nota <= 10:
                return f"Nota válida: {nota:.2f}"  # Retorna a nota formatada com 2 casas decimais
            else:
                print("Erro: A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Erro: Entrada inválida. Tente novamente.")



# 17. Faça uma funçao que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
# Exemplos de saídas com as entradas "user" "user" "user123" respectivamente
# "Erro: A senha não pode ser igual ao nome de usuário. Tente novamente."
# "Usuário e senha cadastrados com sucesso!"
def validar_usuario_senha():
    pass


# 18. Faça um Programa que calcule a média aritmética de um conjunto de N notas.
def media_notas(notas):
    if not notas:
        print("Lista vazia.")
    return sum(notas) / len(notas)



# 19. Faça um programa que mostre os n termos da Série a seguir:
#     S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
def calcular_serie(n):
    i = 1
    m = 1
    soma = 0
    for i in range(i, n, 1):
        soma = soma + i / (m)
        m = m + 2
    return soma


# 20. Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
#  A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas 
# dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima 
# informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
# Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
# Atleta: João Silva
# Nota: 7.9
# Nota: 8.5
# Nota: 9.4
# Nota: 7.0
# Nota: 8.8
# Nota: 9.8
# Nota: 7.9

# Resultado final:
# Atleta: João Silva
# Melhor nota: 9.8
# Pior nota: 7.0
# Média: 8.50
def calcular_media_ginastica():
    pass

# 21. Faça um Programa que desenhe uma pirâmide alinhada à esquerda.
def piramide_esquerda(n):
    x = ""
    for i in range(0,n,1):
      x = x + ("#" * (i + 1)) + "\n"
    return x

print(piramide_esquerda(3))

# 22. Faça um Programa que desenhe uma pirâmide alinhada à direita.
def piramide_direita():
    pass

# 23. Faça um Programa que desenhe duas pirâmides lado a lado.
def piramides_lado_a_lado():
    pass

# 24. Faça um Programa que calcule o troco com a menor quantidade de moedas possível.
def calcular_troco():
    pass

# 25. Faça um Programa que valide um número de cartão de crédito usando o algoritmo de Luhn.
def validar_cartao():
    pass
