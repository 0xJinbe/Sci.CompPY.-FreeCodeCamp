#loop and iterations

x = 2
while x > 0:
    print(x)
    x = x - 1
print('Blastoff! ')
print(x)
#infinite loop
#n = 5
#while n > 0:
#    n = n - 1 stop the loop statement (5-1 até chegar no 0)
#   print('Lather')
#    print('Rinse')
#print('Dry off!')

while True:
    line = input('digite aqui > ')
    if line == 'done' :
        break
    print(line)
print('Done! ')
##############
#definate loops

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff! ')
########
friends = ['Joseph', 'Glenn', 'Sally']
for friends in friends:
    print('Happy New Year: ', friends)
print('Done! ')

#loop idioms(patterns)

print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')
####################
largest_so_far = -1
print('Before' , largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
print('#############################')
#more loop patterns

zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
#calculo do total de iterations, calculo do total da soma dos values, calculo da media da soma (values) por n(iterations)
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, "is...", sum/count)

#filtering in a loop

print('Before')
for value in [9, 41, 12, 3, 74, 15, 21, 22, 23]:
    if value > 20:
        print('Large number', value)
print('After')

#Search using a boolean Variable

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

#Encontrando menor valor

smallest_so_far = -1
print('Before', smallest_so_far)
for the_num in [9, 41, 12, -2, 74, 15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
        print(smallest_so_far, the_num)
print('After', smallest_so_far)

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

#loops in strings

fruit = 'banana'
for letter in fruit:
    print(letter)
letter = fruit[1]
print(letter)
x= 3
w = fruit[x - 1]
print(w)
x = len(fruit)
print(x)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1
#contando letras com o loop na string banana
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
#more string operations
#recortando
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[:])

#encontrando letras em strings
fruit = 'banana'
print('n' in fruit)
if 'a' in fruit:
    print('Found It! ')
print(dir(fruit))

#find and replace on a string

greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print(nstr)
nstr = greet.replace('o', 'x')
print(nstr)
#tirando white spaces
greet = '   Hello Bob'
print(greet.strip())

#exercicio encontrando numa frase
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)




