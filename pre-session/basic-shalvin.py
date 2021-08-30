'''
Created By: Shalvin Narayan
Email: shalvin.narayan@gmail.com
Date: 30 August 2021
'''

number = 6677 #integer

number_decimal = 18.6 #double or float

height = 1.8 #double or float

name = 'Shalvin Narayan' #string

print(number)
print(number, ' is number')
print(number_decimal, ' is decimal number')
print(height, ' is height')
print(name)
print(name, ' is my name')

print('--------Lets calculate area of a cirle----------')

radius = 12.25

pi = 3.14

area_circle = pi * radius * radius

print(area_circle, ' is area of the circle')

print('----------Lets calculate area of triangle--------')

#triange (ask user for input)

print('Please enter the base: ')
base = input()

print('Please enter the height: ')
height = input()

print(base, height, 'is the base and height, respectively')

area_triangle = 0.5 * float(base) * float(height)

print(area_triangle, ' is the area of the triangle')