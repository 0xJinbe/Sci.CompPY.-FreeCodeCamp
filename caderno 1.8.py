#interação com for e in range:
name = input('Enter a name: ')
number = int(input('Enter a number: '))

for i in range(0, number):
    print(name)

#Iteração com for pela string gerada no input - 037

name = input('Enter your motherfucking name: ')
for i in name:
    print(i)
#loop no loop. """ Change the program 037 to also ask for a number. Display their name (one letter at a time on each
#line) and repeat this for the number of times they entered. """

name = input('Enter your motherfucking name: ')
number = int(input('Enter a number: '))

for x in range(0, number):
    for i in name:
        print(i)

#dicts - keys and values

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

#overwriting lists and dicts

lst = list()
lst.append(12)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

#dict - common aplications - histograma, counting number on names

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#the GET method for dictionaries - faz mesma coita que em cima (conta e guarda adicionando)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#counting words in a text

counts = dict()
print('Enter a line of text: ')
line = input(' ')

words = line.split()

print('Words: ', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

#definite loops and dictionaries

counts = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])

print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items()) #cria tuplas

#BONUS: 2 ITERATIONS VARIABLES - first is the key, second is the value

jjj = {'joao': 1 , 'jose': 42 , 'maria': 100}
for aaa,bbb in jjj.items():
    print(aaa, bbb)

#contando palavras dentro de um arquivo usando 2 nested loops

name = input('Enter a file: ')
handle = open(name)

counts = dict() #criando white dict
for line in handle:
    words = line.split()  #separando as palavras das linhas
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # chave para fazer contagem (histograma)

bigcount = None #igualando variaveis a zero #MAX LOOP
bigword = None
for word,count in counts.items(): #loop c 2 iteration variables e .items para crias tuplas
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


