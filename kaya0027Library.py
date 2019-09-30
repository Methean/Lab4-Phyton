import math
import unittest
class TestFunctions(unittest.TestCase):


# 1st Task
def calculateMpg(miles_int, gallons_int):
    return miles_int / gallons_int


miles_string = input("Enter the amount of miles you went.")
gallons_string = input("Enter the number of gallons you consumed.")
miles_int= int(miles_string)
gallons_int= int(gallons_string)

Mpg = calculatingMpg(miles_int , gallons_int)

# "The above program will calculate the Mpg of a car.

#2nd Task
from math import pi

def calculateAreaofCircle(radius_int):
    return pi*math.pow(radius_int, 2)



radius_string = input("Please enter the value of radius.")
radius_int = int(radius_string)
AoC= calculateAreaofCircle(radius_int)

#The above program will calculate the area of a Circle.

# 3rd Task
def convertFahrenheitToCelcius(fahrenheit_int):
    return (fahrenheit_int - 32) / 1.8

fahrenheit_string = input("Please enter the value of Fahrenheit.")
fahrenheit_int = int(fahrenheit_string)
cFTC=convertFahrenheitToCelcius()

#The above prograam will convert Fahrenheit to Celcius.

#4th task
def  calculateDistanceBetweenPoints(x, y, x1, y1)

    return math.sqrt(((x1-x)*(x1-x)) + ((y1-y)*(y1-y)) )

x_string= input("Please enter the x value.")
y_string= input("Please enter the y value.")
x1_string= input("Please enter the x1 value.")
y1_string= input("Please enter the y1 value.")

x=int(x_string)
y=int(y_string)
x1=int(x1_string)
y1=int(y1_string)

cDBP= calculateDistanceBetweenPoints()

#The above function will calculate the distance between two points using Phytagoras formulate.

print("If a car went {0} miles by using {1} amount of "
      "gas. The car can go {2} miles per gallon.".format(miles_int , gallons_int, Mpg))

print("Area of a circle with the radius {0}, is {1}.".format(radius_int, AoC))

print("{0} fahrenheits is equal to {1} celcius.".format(fahrenheit_int, cFTC))

print("The amount of distance between the points ({0},{1}) and ({2}, {3}), is {4}.".format(x,y,x1,y1,cDBP))

#The testing is done below.



unittest.calculateMpg()
unittest.calculateAreaofCircle()
unittest.convertFahrenheitToCelcius()
unittest.calculateDistanceBetweenPoints()