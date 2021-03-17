#exercicios py. Python by Example Learning to Program in 150 Challenges

age = int(input('What is your age?\n>>> '))
if age >= 18:
    print('You can vote.')
elif age == 17:
    print('You can learn to drive')
elif age == 16:
    print('You can buy a lottery ticket')
else:
    print('You can go Trick-or-Treating ')

#""" Ask the user to enter a number. If it is under 10, display the message "Too low", if it their
#number is between 10 and 20, display "Correct", otherwise display "Too high". """

num = int(input('Enter a number: '))

if num < 10:
    print('Too low.')
elif 10 > num < 20:
    print('Correct')
else:
    print('Too high')

#""" Ask the user to enter 1, 2, or 3. If they enter a 1, display the message "Thank you", if
#they enter a 2, display "Well done", if they enter a 3, display "Correct". If they enter anything
#else, display "Error message". """

number = int(input('Enter a number 1, 2 or 3: '))


if number == 1:
    print('Thank you')
elif number == 2:
    print('Well done')
elif number == 3:
    print('Correct')
else:
    print('Error message.')

#""" Ask the user to enter their first name and then display the length of their name. """

name = input('What´s your first name?\n>>> ')

print('Your name has...', len(name), 'letters.')

#""" Ask the user to enter their first name and then ask them to enter their surname. Join them together
#with a space between and display the name and the length of whole name. """

name = input('What´s your first name?:').title()
surname = input('What´s your surname?').title()

name_surname = name + ' ' +  surname
print('Your name is', name_surname, 'your letter count is:', len(name_surname))

#""" Ask the user to enter their first name and surname in lower case. Change the case to title case and
#join them together. Display the finished result. """

name = input('Enter your name: ').lower()
surname = input('Enter your surname: ').lower()

name_surname = name + ' ' + surname
title_name_surname = name_surname.title()
print(title_name_surname)

#""" Ask the user to type in the first line of a nursery rhyme and display the length of the string.
#    Ask for a starting number and an ending number and then display just that section of the text
 #   (remember Python starts counting from 0 and not 1). """




rhyme = input('Enter with a nursery rhyme: ').capitalize()

print('Your rhyme is: ', len(rhyme), 'characters.')
num_1 = int(input('Enter a starting number: '))
num_2 = int(input('Enter a ending number: '))

print(rhyme[num_1:num_2])