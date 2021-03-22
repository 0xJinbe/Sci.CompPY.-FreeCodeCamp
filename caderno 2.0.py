#""" Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names
#and after each name display "[name] has been invited". If they enter a number wich is 10 or higher, display the
#message "Too many people"."""

inp = int(input('How many people do you want in your party? \n'))
if inp < 10:
        for i in range(0, inp):
            names = input('What are their names?\n')
            print(names, 'has been invited. ')
else:
    if inp >= 10:
        print('Too many people.')
print('Invintings done...')

#""" Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add
#that number to the total and print the message "The total is...[total]". Stop the loop when the total is
#over 50. """


total = 0

while total <= 50:
    number = int(input('Enter a number below 50: \n'))
    total += number
    print('Total: ', total)
#""" Ask the user to enter a number. Keep asking until they enter a  value over 5 and then display
#the message "The last number you entered was a [number]" and stop the program. """

number = 0

while number <= 5:
    number = int(input('Enter a number:\n>> '))
print('The last number you entered was a', number, 'and stop the program.')

#""" Ask the user to enter a number and then enter another number. Add these two numbers together and then
#ask if they want to add another number. If they enter "y", ask them to enter another number and keep
#adding numbers until they do not answer "y". Once the loop has stopped, display the total. """



number_1 = int(input('Enter a number:\n>> '))

total = number_1

answer = 'y'

while answer == 'y':
    number_2 = int(input('Enter another number:\n>> '))
    total += number_2
    answer = input('Do your want to enter another number? [y/n]\n>> ').lower()

print(f'The total is {total}')

#""" Ask for the name of somebody the user wants to invite to a party. After this, display the message
#"[name] has now been invited" and add 1 to the count. Then ask if they want to invite anyone else to the
#party and then display how many people they have coming to the party. """

count = 0
answer = 'y'

while answer == 'y':
    name = input('Enter a name you want to invite: ').title()
    print(name, 'has been invited...')
    count += 1
    answer = input('Do you want to invite someone else? y/n ').lower()

print('Count is:', count)

#""" Create a variable called compnum and set the value to 50. Ask the user to enter a number.
#While their guess is not the same as the compnum value, tell them if their guess is too low
#or too high and ask them to have another guess. If they enter the same value as compnum, display
#the message "Well done, you took [count] attempts". """


compnum = 50
count = 0
guess = int(input('Guess a number: '))

while guess != compnum:
    if guess < 50:
        print('Your guess is too low...')
    else:
        print('Your guess is too high...')

    guess = int(input('Make another guess: '))
    count += 1
print('The guess is done. You took:', count, 'attempts.')

#""" Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message
#"Too low" and ask them to try again. If they enter a value above 20, display the message "Too high" and ask
#them to try again. Keep repeating this until they enter a value that is between 10 ans 20 and then display
#the message "Thank you". """



num = int(input('Enter a number between 10 and 20. '))

while num < 10 or num > 20:
    if num < 10:
        print('TOO LOW')
    else:
        print('TOO HIGH')
    num = int(input('Try again: '))

print('Thank you.')


#ultimo exercicio de while

num_bottles = 10

while num_bottles > 0:

    print(
        f'There are {num_bottles} green bottles hanging on the wall, {num_bottles} green bottles hanging on the wall, and if 1 green bottle should accidentally fall.\n')

    num_bottles -= 1

    user_answer = int(input('How many green bottles will be hanging on the wall?\n>> '))

    if user_answer == num_bottles:
        print(f'There will be {num_bottles} green bottles hanging  on the wall\n')

    else:
        while user_answer != num_bottles:
            user_answer = int(input('No, try again:\n>> '))

print('There are no more green bottles hanging on the wall')

