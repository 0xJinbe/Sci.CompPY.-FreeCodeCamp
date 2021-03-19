""" Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an "ay".
If a word begins with a vowel you just add "way" to the end. For exemple, pig becomes igpay, banana
becomes ananabay, and aadvark becomes aadvarkway. Create a program that will ask the user to enter
a word and change it into Pig Latin. Make sure the new word is displayed in lower case. """

word = input('Enter a word: ')
first = word[0]
lenght = len(word)
rest = word[1:lenght]
if first == 'a' and first == 'e' and first == 'i' and first == 'o' and first == 'u':
    new_word = rest + first + 'ay'

else:
    new_word = word + 'way'
print(new_word.lower())


number = int(input('Enter a number between 1 and 12:\n >>'))

for i in range(1, 13):
    print(f'{i} X {number} = {i * number}')

#""" Ask for a number below 50 and then count down from 50 to that number, making sure you show the number
#they entered in the output. """


number = int(input('Enter a number below 50: '))
for i in range(50, number-1, -1):
    print(i)

#""" Ask the user to enter their name and a number. If the number is less than 10, then display
#their name that number of times; otherwise display the message "Too high" three times. """

name = input('Enter your name: ')
number = int(input('Enter a number asshole: '))

if number < 10:
    print(name * number )
else:
    print('Too high' * 3)

#Set a variable called total as 0. Ask to the user to enter five numbers and after each input ask them
#if they want that number included. If they do, then add the number to the total. If they do not want it
#included, don't add it to the total. After they have entered all five numbers, display the total. """


total = 0

for i in range(0, 5):
    number = int(input('Enter a number:\n>> '))
    answer = input('Do you want to add this number? (y/n)\n>> ').lower()
    if answer == 'y':
        total += number
        print(total)
#""" Ask which direction the user wants to count (up or down). If they select up, then ask them for the top number
#and then count from 1 to that number. If they select down, ask them to enter a number below 20 and then count down
#from 20 to that number. If they entered something other than up or down, diplay the message "I don't understand"."""



user_direction = input('Do you want to count up or down: ')

if user_direction == 'up':
    top_number = int(input('Enter a top number: '))
    for i in range(1, top_number +1):
        print(i)
if user_direction == 'down':
    bottom_number = int(input('Enter a number below 20: '))
    for i in range(20, bottom_number -1, -1):
        print(i)
else:
    print('I dont understand...')
