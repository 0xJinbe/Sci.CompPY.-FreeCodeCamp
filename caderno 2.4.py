#exercícios sobre random

#""" Display a random fruit from a list of five fruits. """

from random import choice
fruit = choice(['banana', 'maça', 'abacate', 'laranja', 'mamao'])
print(fruit)

#""" Randomly choose either heads or tails ('h' or 't'). Ask the user to make their choice. If their choice is the
#same as the ramdomly selected value, display the message "You wim", otherwise display "Bad luck". At the end, tell
#the user if the computer selected heads or tails. """

from random import choice

computer_choice = choice(['t','h'])

user_choice = input('Make a choice: t or h: ')
if user_choice == computer_choice:
    print('YOU WIN')
else:
    print('BAD LUCK')
if computer_choice == 'h':
    print('ITS HEADS')
else:
    print('ITS TAILS')

#""" Randomly choose a number between 1 and 5. Ask the user to pick a number. If they guess correctly, display the message "Well done",
#otherwise tell them if they are too high or too low and ask them to pick a second number. If they guess correctly on their second guess,
#display "Correct", otherwise display "You lose". """

from random import randint

computer_number = randint(1,5)
user_number = int(input('Enter a number between 1 and 5: '))
if user_number == computer_number:
    print('WELL DONE')
else:
    if user_number < computer_number:
        print('You number is too low...')
    elif user_number > computer_number:
        print('Your number is too high...')
    user_number2 = int(input('Enter another number: '))
if computer_number == user_number2:
    print('Correct')
else:
    print('you lose')

#""" Randomly pick a whole number between 1 and 10. Ask the user to enter a number and keep entering numbers until
#they enter the number that was randomly pickerd. """

from random import randint
comp_number = randint(1, 10)
u_numb = int(input('Enter a number from 1 to 10: '))
while u_numb != comp_number:
    if u_numb < comp_number:
        print('number too low')
    else:
        print('number too high')
    u_numb = int(input('Your number is wrong, enter another number: '))

print('YOU GUESSED THE RIGHT NUMBER...')

#""" Make a maths quiz that asks five questions by randomly genereting two whole number to make the question
#(e.g. [num1] + [num2]). Ask the user to enter the answer. If they get it right add a point to their score. At
#the end of the quiz, tell them how many they got correct out of five. """

score = 0

for i in range(1,6):   #scrip para ajudar em calculos matematicos de soma :))
    num1 = randint(1,50)
    num2 = randint(1,50)
    print(f"{num1} + {num2}")
    computer_answer = num1 + num2
    user_answer = int(input('>>'))
    if user_answer == computer_answer:
        score = score + 1
print(f'Total score = {score}')

#""" Display five colours and ask the user to pick one. If they pick the same as the program has chosen,
# say "Well done", otherwise display a witty answer wich involves the correct colour, e.g. "I bet you are
# GREEN with envy" or "You are probaly felling BLUE right now". Ask them to guess again; if they have still
# not got it right, keep giving them the same clue and ask the user to enter a colour until they guess it correctly. """

colours_choice = choice(['red', 'blue', 'yellow', 'white', 'black'])

while True:
    user_choice = input("Select from: red, blue, green, pink and white\n>>").lower()
    if user_choice == colours_choice:
        print('Well done...')
        break
    else:
        if colours_choice == 'red':
            print('Bet your eyes are RED of anger...')
        elif colours_choice == 'blue':
            print('Are you feeling blue? ')
        elif colours_choice == 'yellow':
            print('Bananas are...')
        elif colours_choice == 'white':
            print('What´s your wall´s colour?')
        elif colours_choice == 'black':
            print('Black METAL RULES...')








