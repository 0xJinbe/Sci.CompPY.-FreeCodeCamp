#Lists

#iteration on a list
z = [ 'Jose', 'Glen', 'Sally']
for x in z:
    print('Happy new year: ', x)
print('Done')
#Itinerando com for in range
for i in range(len(z)):
    x = z[i]
    print('Happy New Year: ', x)
#concatenating lists using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
#list slice
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
#methods in lists
#print(dir(t))
#building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('xablaus')
#is something in a list?
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)
#lists are in order #alfabetical ordering
friends = ['Jose', 'Glen', 'Sally']
friends.sort()
print(friends)
print(friends[1])
#built in functions and lists
nums = [3, 41, 12, 9 ,74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))
#looping with input and finding average

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
average = total/count
print('Average: ', average)

numlist = list()
while True:
    inp = input('Enter a numer: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average: ', average)



