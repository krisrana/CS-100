'''
Krishna Rana
CS 100 2018S Section 108
HW 02, Febuary 8th, 2018
'''
#PLEASE UNDO THE MULTIPLE LINE COMMAND ONE AT A TIME TO RUN THE CODE.
'''
import turtle
screen = turtle.Screen()
screen.setup(800,800)
T = turtle.Turtle()
T.pencolor('red')
'''
#Question 1
#turtle graphics command to draw Equilateral triangle.
'''
for i in range(1,4):
    T.fd(100)
    T.lt(120)
'''
#turtle graphics command to draw a square.
'''
for i in range(1,5):
    T.fd(100)
    T.lt(90)
'''
#turtle graphics command to draw a regular pentagon.
'''
for i in range(1,6):
    T.fd(100)
    T.lt(72)
'''

#Question 2
#turtle graphics command to draw concentric cirle with radius 50, 100, 150, and 200
'''
#instantiation of the value
coordinate = 0 #setting y value of position to 0 initially
radius = 50 #setting initail radius as 50
for i in range(1,5): #loop will run 4 time, giving circles of radius of 50,100,150,200.
    T.penup()   
    T.setpos(0,coordinate)   
    T.pendown()   
    T.circle(radius)
    coordinate = coordinate - 50 #co-ordinate is being moved -50 position every loop call
    radius = radius + 50 #radius is incremented by 50 every loop call
'''
#Question 3
'''
import math
print("The Factorial of 100 is:",math.factorial(100))
print("The log(base 2) of 1,000,000 is:",math.log(1000000,2))
print("The greatest common denominator of 63 and 49 is:",math.gcd(63,49))
'''
