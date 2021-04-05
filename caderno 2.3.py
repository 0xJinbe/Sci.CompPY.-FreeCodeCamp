# Projeto basico Voitto plotar grafico

#Questao 1: crie uma lista usando o for que armazene apenas os quadrados dos números pares de 1 a 10

lista_pares = []
for i in range(1,11):
    if i % 2 == 0:
        lista_pares.append(i**2)
print(lista_pares)
#para o mesmo problema faça usando o list comprehension

lc_pares = [i**2 for i in range (1,11) if i % 2 == 0]
print(lc_pares)

#Questao 2: crie uma funçao def que receba como parametro. uma lista de 10 numeros 1 a 20. uma função lambda qe calcula raiz quadrada
#por fim def deve retornar uma lista com o resultado das raizes de cada um dos numeros da lista passada como parametro

def raizes(numeros, f):
    num_raizes = []
    for i in numeros:
        num_raizes.append(f(i))
    return num_raizes

lista_num = range(10,21)
r = raizes(lista_num, lambda x: x**(1/2))
print(r)

#fazendo mesma coisa com list comprehension

def raizes_lc(x, func):
    return [func(i) for i in x]
def raiz_quadrada(x):
    return x**0.5
r2 = raizes_lc(lista_num, raiz_quadrada)
print(r2)

#fazendo utilizando função de biblioteca math

import math
math.sqrt

r3 = raizes_lc(range(10,21), math.sqrt)
print(r3)

#mais uma solução utilizando dicionário (mais facil pra visualizar a lista)
def raizes_dc(numeros, f):
    num_raizes = {}
    for i in numeros:
        num_raizes[i] = f(i)
    return num_raizes
dicionario = raizes_dc(list(range(10,21)), math.sqrt)
print(dicionario)
print(dict(a = r2))




#Questao 3: escreva uma funcao def que receba com parametro o inicio e o fim de um intervalo e crie uma lista com os valores dentro desse intervalo
#incluindo o valor final. dentro dessa mesma função crie outra lista contendo os quadrados dos valores da primeira lista.
#retorne as duas listas

def quadrado(inicio, fim):
    l = range(inicio, fim+1)
    q = [i**2 for i in l] #itinerando um list comprehension em outra lista
    return l, q
num, quad = quadrado(1, 10)
print(num,quad)

#com as listas criadas anteriormente crie um grafico e veja como ficam distribuidos. em seguida salve o grafico

import matplotlib.pyplot as plt
plt.plot(num)
plt.plot(quad)
plt.show()

