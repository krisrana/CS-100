#Question 5a
'''
Krishna Rana
CS 100 2018S Section 108
HW 00, Jan 22, 2018
'''
#Question 5b
daysInYear = 365
weeksInYear = 52
monthsInYear = 12
daysInWeek = 7

#Question 5c
percentage = 0.01
intrestRate = 0.25
length = 5.76

#Question 5d
myName = 'Krishna Rana'
favouriteMovie = 'Star Wars Series'
hobby = 'Basketball'

#Question 6
#Exercise 1-1
print(">>> Answer's for Chapter #1, Exercise 1 and 2 \n")
'''
# 1
print( - If we leave out the 2nd parentheses, the shell will indent to next line when enter is pressed.
print) - If we leave out the 1st parentheses, we will have a syntax error saying, "SyntaxError: invalid syntax".
print - If we leave out both parentheses we get this as output, "<built-in function print>".

# 2
print("hello) - If we leave out the 2nd quotation mark we get, "SyntaxError: EOL while scanning string literal".
print(hello") - If we leave out the 1st quotation mark we get the same error as the first one,
"SyntaxError: EOL while scanning string literal".
print(hello) - If we leave out both of the quotation mark we get, the following error,
                Traceback (most recent call last):
                  File "<pyshell#14>", line 1, in <module>
                    print(hello)
                NameError: name 'hello' is not defined

# 3
+2 - This input yields the result as 2, so the output is simply the number removing the positive sign.
2++2 - This inout yields the result as 4, So the output is simply the additon of the numbers. Python interpreter
        take the 1st "+" sign as an operator and 2nd "+" sign as an positive number to be added to the 1st number.

# 4
09 - when a leading zero in pyhton is used we get an Syntax error saying, "SyntaxError: invalid token".

# 5
5 4 or 9 8 - when we have 2 values with no operator between them we get an syntax error saying,
            "SyntaxError: invalid syntax"
'''
#Exercise 1-2
# 1
totalSeconds = 0
minutes = 42
oneMinute = 60 #seconds
seconds = 42

#Calculation for total seconds
totalSeconds = (minutes * oneMinute) + seconds
#output
print("There are", totalSeconds, "seconds in", minutes, "minutes and", seconds, "seconds.")

#2
totalMiles = 0
kilometers = 10
oneMile = 1.61 #kilometers

#Calculation for total miles
totalMiles = kilometers / oneMile
#output
print("There are %.2f" % totalMiles, "miles in", kilometers, "kilometers.")

#3
averagePacePerMin = 0
averagePacePerSec = 0
averageSpeedPerHour = 0

#Calculation for average pace per minute
averagePacePerMin = (totalSeconds / totalMiles) // 60
#Calculation for average pace per second
averagePacePerSec = (totalSeconds / totalMiles) % 60
#Calculation for average speed in mile per hour
averageSpeedPerHour = (totalMiles * oneMinute * 60) / totalSeconds
#output
print("The average pace time per mile is %.2f" % averagePacePerMin, "minutes and %.2f" % averagePacePerSec,"seconds.")
print("The average speed is %.2f" % averageSpeedPerHour, "miles per hour.")

############################
#Chapter 2
print("\n>>> Answer's for Chapter #2, Exercise 1 and 2 \n")
#Exercise 1
'''
42 = n - when we put the nummber first and than the varible name we get, SyntaxError: can't assign to literal.

x = y = 1 >>> print(x, y) >>> 1 1 -  This is legal assignment in python, x and y are assigne the value of 1.

x = y = 1; >>> word = "hello"; >>> name = 'me'; - semi-colon does not create any syantax error, it is ok with python.

word = "maybe". - when you put a period at the end of a statment we get, SyntaxError: invalid syntax.

x=1 >>> y=2 >>> xy   Traceback (most recent call last):
                        File "<pyshell#12>", line 1, in <module>
                xy    NameError: name 'xy' is not defined
                x y   SyntaxError: invalid syntax
When we try to multiple x and y, like we can in math notation in python, we get the error mentioned above. it gives us a NameError,
python thinks that "xy" is a variable which is not yet defined. so if we want to multiple we need to use the * operator.
'''
#Exercise 2
#1
volumeOfSphere = 0.0
pi = 3.14
radius = 5

#formula layout for calcuating volume of sphere
volumeOfSphere = ((4.0/3.0) * pi * (radius ** 3))
#output
print("The volume of sphere with radius", radius, "is %.2f" % volumeOfSphere)

#2
coverPrice = 24.95
discount = 0
discountPrice = 0
shippingCostOneCopy = 3
shippingCostMoreCopy = 0.75
totalShippingCost = 0
numberOfBooks = 60
wholesaleCost = 0

#Calculation
discount = coverPrice * (40/100) #Finds the discount price amount to be deducted from cover price
discountPrice = coverPrice - discount #finds the final discounted price
totalShippingCost = 3 + (shippingCostMoreCopy * (numberOfBooks - 1)) #find the shipping cost for number of Books
wholesaleCost = discountPrice * numberOfBooks + totalShippingCost #find the wholesale Cost for number of books
#output
print("The total wholesale cost for", numberOfBooks, "books is $%.2f" % wholesaleCost)

#3
leftHome = (6 * 60 * 60) + (52 * 60) #all time is in seconds
easyPace = (8 * 60) + 15 #time converted in seconds
tempoPace = (7 * 60) + 12 #time converted in seconds
#calculating total running time in seconds
totalTime = (2 * easyPace) + (3 * tempoPace)
#calculating time back home for breakfast in second
backHome = leftHome + totalTime
#converting seconds to hours
timehour = backHome / 60 / 60
#converting seconds to seconds under one min(60).
timeSec = backHome / 60 % 60
#output
print("The time you get home for breakfast will be %d:%d" % (timehour,timeSec))
