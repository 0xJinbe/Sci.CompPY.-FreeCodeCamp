#call de dicts
my_dict = {'a':'1,3,5,7,12', 'b':'gosto de metal'}
print(my_dict['a'])
print(my_dict['b'].upper())
print(my_dict['a'][0])
print(my_dict['a'][-3])
print(my_dict['a'][2:])
#dict vazio
c = {}
c['faisca'] = 'meu+cachorro'
c['resposta'] = '42'
print(c['faisca'])
#dict keys and values
d = {'chave1':1, 'chave2':2, 'chave3':3}
chaves_tds = d.keys()
print(chaves_tds)
valores = d.values()
print(valores) == print(d.values())
print(d.items())

#clone de calculo deslocamento (duvida sobre a Terra)
#distância = float(input("Digite a distância em km:"))
#velocidade_média = float(input("Digite a velocidade média em km/h:"))
#tempo = distância / velocidade_média
#print("O tempo estimado é de %5.2f horas" % tempo)
# Opcional: imprimir o tempo em horas, minutos e segundos
#tempo_s = int(tempo * 3600) # convertemos de horas para segundos
#horas = int(tempo_s / 3600) # parte inteira
#tempo_s = int(tempo_s % 3600) # o resto
#minutos = int(tempo_s / 60)
#segundos = int(tempo_s % 60)
#print("%05d:%02d:%02d" % (horas, minutos, segundos))


#call de tuples
t = (1,2,3,4,5,6,7,8,9,0)
print(len(t))

print(t.index(8))
print((t)[7])
print(t[-2])
print(t[-4])
print("------")
t.count("2")

#aplicando funçoes em variaveis
print('0-----------0')
a = 'araraquara'
b = ['1,2,3,4']
print(b.reverse())
print(a.upper())


#inicio de call de classes
class  cachorros:
    cobertura = "pelos"
    alimento = 'carne'
    habitat = 'domestico'
    patas = 4
    nome = 'rex'
class galinhas:
    cobertura = 'penas'
    alimento = 'graos'
    habitat = 'domestico'
    patas = 2
    bico = 'pequeno'

print(dir(cachorros))
print(dir(galinhas))

faisca = cachorros()
lala = galinhas()

print(faisca.alimento)

print(faisca.habitat)

print('========================')

#condicionais
x=18

if x < 2:
    print('small')
elif x < 10:
    print('medium')
else:
    print("LARGE")
print('all done')

print('==============================')

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice Work')
else:
    print('Not a number')

print('---------------------------------')
def thing():
    print('HEllo')
    print('fun')

print(thing())

def greet(lang):
    if lang == 'es':
        return 'hola'
    elif lang =='fr':
        return 'Bounjour'
    else:
        return 'HELLO'

print(greet('en'), 'Glenn')
print(greet('fr'), 'Silvia')

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)

print('------------- ')