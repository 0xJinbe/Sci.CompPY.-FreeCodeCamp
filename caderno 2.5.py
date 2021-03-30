#Tuples

#sorting lists of tuples:

d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
#dict_items([('a',10), ('c', 22), ('b', 1)])
print(sorted(d.items()))  #sorting the dict by keys. a,b,c...

#using sorted

t = sorted(d.items())
for k,v in sorted(d.items()): #sorted by key
    print(k,v)
#sorted by values instead of keys

c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k,v in c.items():
    tmp.append( (v,k) )  #criando uma lista em que os valores das tuplas vem primeiro
print(tmp)

tmp = sorted(tmp, reverse=True) #sorting in reverse
print(tmp)

#TOP 10 MOST COMMMON WORDS

fhand = open(r'C:\Users\Germano\Downloads\bio.autor.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
#listcomprehension = print(sorted([(v,k) for k,v in c.items()]))
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

#REGULAR EXPRESSIONS pratical aplications
import re

lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin) #assim como list comprehension pelas expressoes se recorta mais facil
print(y)
#maneira 'normal' de se fazer usando double split

a = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
palavras = a.split() #separa a
print(palavras)
email = palavras[1] #escolhe o index certo
print(email)
pedaço = email.split('@') #separa o index
print(pedaço[1])

#Network sockets HTTP
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('...', 80))

#Writing a simples web browser...

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()