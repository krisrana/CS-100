'''
Krishna Rana
CS 100 2018S Section 108
HW 03, Febuary 8th, 2018
'''
#PLEASE UNDO THE MULTIPLE LINE COMMAND ONE AT A TIME TO RUN THE CODE.
#Question 1
#undo below
'''
#i.
a = 3
b = 4
c = 5
print("Answer: 1\n")
#ii.
if(a < b):
    print("ii. - OK")

#iii.
if(c < b):
    print("iii. - OK")
    
#iv.
sum1 = a + b
if(sum1 == c):
    print("iv. - OK")

#v.
asquared = a*a
bsquared = b*b
csquared = c*c

sum2 = asquared + bsquared
if(sum2 == csquared):
    print("v. - OK")
'''
#<<undo above

#<<undo below
'''
#Question 2
print("\nAnswer: 2\n")
#ii.
if(a < b):
    print("ii. - OK")
else:
    print("ii. - NOT OK")

#iii.
if(c < b):
    print("iii. - OK")
else:
    print("iii. - NOT OK")
    
#iv.
sum1 = a + b
if(sum1 == c):
    print("iv. - OK")
else:
    print("iv. - NOT OK")
    
#v.
asquared = a*a
bsquared = b*b
csquared = c*c

sum2 = asquared + bsquared
if(sum2 == csquared):
    print("v. - OK")
else:
    print("v. - NOT OK")
'''
#<<undo above

#<<undo below
'''
#Question 3
import turtle
screen = turtle.Screen()
screen.setup(800,800)
T = turtle.Turtle()
#prompt statments
prompt1 = "What color would you like? :"
prompt2 = "What is the width of line you want? :"
prompt3 = "What is the length of line you want? :"
prompt4 = "What shape? - line, triangle or square: "
#keyboard input
color = input(prompt1)
width = input(prompt2)
length = int(input(prompt3))
shape = input(prompt4)
#passing the keyboard value to repective places
T.pencolor(color)
T.pensize(width)
#verifiing shape based on user choice
if(shape == "line" or shape == "Line"):
    T.fd(length)
elif(shape == "triangle" or shape == "Triangle"):
    for i in range(1,4):
        T.fd(length)
        T.rt(120)
elif(shape == "square" or shape == "Square"):
    for i in range(1,5):
        T.fd(length)
        T.rt(90)
else:
    print("Wrong choice")
#hidding turtle after drawing
T.ht()
'''
#<<undo above

#<<undo below
'''
#Question 4
#math module for round function
import math
#prompt statments with keyborad input and string to int conversion
homework = int(input("Enter grade for Homework: "))
midterm1 = int(input("Enter grade for Midterm 1: "))
midterm2 = int(input("Enter grade for Midterm 2: "))
finals = int(input("Enter grade for Final Exam: "))
roadmap = int(input("Enter grade for Roadmap: "))
recitation = int(input("Enter grade for Recitation: "))
misc = int(input("Enter grade for Misc: "))
#calculation for score based on % weight
homework = round(homework * .10)
midterm1 = midterm1 * .20
midterm2 = midterm2 * .20
calculatedFinals = finals * .30
roadmap = roadmap * .10
recitation = recitation * .04
misc = misc * .06
#getting overall grade total for display
overallGrade = homework + midterm1 + midterm2 + calculatedFinals + roadmap + recitation + misc
#converting overallGrade to a rounded number
convertedGrade = round(overallGrade)
#printing overall grade on display
print("Overall grade :",convertedGrade)
#checking final cutoff for grades via if-else conditions and printing message accordingly
if((finals >= 80) and (convertedGrade >= 85)):
    print("You got an A!")
elif((finals >= 75) and (convertedGrade >= 80)):
    print("You got a B+!")
elif((finals >= 70) and (convertedGrade >= 75)):
    print("You got a B.")
elif((finals >= 65) and (convertedGrade >= 70)):
    print("You got a C+..")
elif((finals >= 65) and (convertedGrade >= 65)):
    print("You got a C...")
else:
    print("You failed the course....")
'''
#<<undo above



