#funções (patronização de ações que podem ser usadas em vários lugares)

def calcula_area_circulo(raio):
    pi = 3.14
    area = pi * raio ** 2
    print('A area do círculo é : ', area)

calcula_area_circulo(5)

#def em listas com for

uma_lista_qqr = ['jurídico', 'financeiro', 'RH', 'diretoria']

def imprimes_setores(uma_lista_qqr):
    for setores in uma_lista_qqr:
        print(setores)

imprimes_setores(uma_lista_qqr)

#reutilizando a função com outros parâmetros...

s = ['Marketing', 'Executivo']
imprimes_setores(s)

#definindo parametros opcionais para a função (assim e possivel chamar ela vazia, o parametro ja foi colocado antes)
def pararloop(valor = 5): #valor parametro predefinido para a função
    for i in range(10): #itinerando em 10 posições (valores acima de 10 sao desconsiderados no loop)
        if (i == valor): #colocando condição para parar o loop no valor do parametro colocado
            break
        print(i)
pararloop()
pararloop(2)
pararloop(11)

#tipos de retorno

def calcula_area_circulo(x):
    pi = 3.14
    area = pi * x**2
    return area
a = calcula_area_circulo(2)
print(a)
print(a + 10)

def calcula_quadrado(a):
    return a**2

b = calcula_quadrado(3)
print(b)

v1 = calcula_quadrado(2)
v2 = calcula_area_circulo(3)
print(v1,'---', v2)

#retornos multiplos

def operações_aritméticas(n1, n2):
    soma = n1 + n2
    subtração = n1 - n2
    return soma, subtração
print(operações_aritméticas(2,1))
print(operações_aritméticas(5,2))
#desempacotando a tupla
soma, subtração = operações_aritméticas(10, 2)
soma1, sub1 = operações_aritméticas(6,3)

print(soma, subtração)
print(soma1, sub1)

#função anonima - n vinculada a um indentificador - lambda

f = lambda x: x**2

print(f(2))
print(f(5))

#função f em uma lista (colocando a função lambda **2 na lista_num

list_num = [1,2,3,4,5,6]

for i in list_num:
    print(f(i))
#função que recebe a função lambda

def função(list_num, f):
    for i in list_num:
        print(f(i))
print('------------------------')
função(list_num, lambda x: 2*x)
função([2,3,4,5,6],lambda x: x-10)
print('------------------------------')
print(list_num)

def função2(list_num, f):
    nova_lista = []
    for i in list_num:
        nova_lista.append(f(i))
    return nova_lista
print(função2(list_num, f))

print('------------')

print(função2(list_num, lambda x: x-2))


nl = função2(list_num, f)
print(nl)
print(nl[0:4])

print('---------------')

def função3(list_num, f):
    return[f(i) for i in list_num]

print(função3([2,3,5], lambda x: 2*x))




