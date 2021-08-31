#Created By: Shalvin Narayan
#Email: shalvin.narayan@gmail.com
#Date: 31 August 2021

#This aim of this script is to implement functions and calculate volumes
#by taking user input.

PI = 3.14 #Setting the constane value for PI.

#Defining of the functions

#Function to calculate area of the the circle
def area_circle(radius): #radius is the parameter of the function

    area = PI * pow(radius, 2)

    #print(area, ' is the print statement inside the area_circle function')

    return area

#Function to calculate the volume of the cylinder
def volume_cylinder(radius, height): #radius and height are the parameters of the function

    volume = PI * pow(radius, 2) * height

    return volume

#Function to calculate the volume of the sphere
def volume_sphere(radius): #radius is the parameter of the function

    volume = (4/3) * PI * pow(radius, 3)

    return volume


#Ask user to input the radius
print('Please enter the radius of the circle: ')

radius = float(input()) #Getting the string input from user and casting into float data type

print(radius, ' is the radius')

#Calculating the area of the circle by calling area_circle function
area = area_circle(radius)

print(area, ' is the area of the circle')

#Ask user to input the height
print('Please enter the height of the cylinder: ')

height = float(input()) # Getting the string input from user and casting into float data type

print(height, ' is the height')

#Calculate the volume of the cylinder by calling volume_cylinder function
volume = volume_cylinder(radius, height)

print(volume, ' is the volume of the cylinder')

#Calculate the volume of the sphere by calling volume_sphere function
volume = volume_sphere(radius)

print("{:.2f}".format(volume), ' is the volume of the sphere') #Formatting the volume to 2 decimal place
