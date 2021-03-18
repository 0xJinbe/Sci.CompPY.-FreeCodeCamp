#exercícios

#""" Ask the user to enter a number with lots of decimal places. Multiply this number by two and and display
#the answer. """

number = float(input('Enter a number with a lot of decima places: '))

print(number * 2)
print(round(number, 2))

#""" Ask the user to enter an integer that is over 500. Work out the square root of that number and
#display it to two decimal places. """

from math import sqrt

integer = int(input('Enter a integer over 500: '))
print(round(sqrt(integer), 2))

#""" Display (pi) to five decimal places. """
from math import  pi
print(round(pi, 5))

#""" Ask the user to enter the radius of a circle (measurement from the centre point to the edge). Work
#out the area of the circle (pi * radius ** 2). """

radius = float(input('Enter the radius: '))
area = pi * radius ** 2
print(area)

#""" Ask for the radius and the depth of a cylinder and work out the total volume (circle area * depth)
#rounded to three decimal places. """

radius = float(input('Enter radius of the cilinder: '))
depth = float(input('Enter deth of the cilinder: '))

vol = (pi * radius ** 2) * depth
print('Your cilinder vol is: ', (round(vol, 3)))

#""" Ask the user to enter two numbers. Use whole number division to divide the first number by the second
#and also work out the remainder and display the answer in a user-friendly way (e.g. if they enter 7 and
#2 display "7 divided by 2 is 3 with 1 remaining"). """

first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))

div = first / second
remainder = first % second

print(first, 'divided by', second, 'is: ', div, 'with', remainder, 'remaining.' )

#""" Display the following message:
          #  1) Square
          #  2) Triangle
   # Enter a number:
#If the user enters 1, then it should ask them for the length of one of its sides and display the area.
#If They select 2, it should ask for the base and height of the triangle and display the are. If they
#type in anything else, it should give them a suitable error message. """

user_answer = int(input('1) Square\n 2) Triangule\n Enter a number: \n>>'))

if user_answer == 1:
    lenght = float(input('Lenght of its sides: '))
    print('The area of your chosen shape is: ', lenght ** 2)
if user_answer == 2:
    base = int(input('What´s the base of the triangle? '))
    height = int(input('Whats the height of the triangle? '))
    area = base * height / 2
    print('The area of your chosen shape is: ', area)
else:
    print('An error ocurred...')



