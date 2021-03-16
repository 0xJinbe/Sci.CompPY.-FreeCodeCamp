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


