'''
Krishna Rana
CS 100 2018S Section 108
HW 01, Febuary 1, 2018
'''
#QUESTION 2
print("Answers of Question 2\n")
#declaration of list's named grades and frequency
grades = ['A', 'A', 'A', 'B', 'B', 'C', 'A', 'D', 'C', 'F']
frequency = list()
#for loop to iterate throughout the list
for grade in ['A','B','C','D','F']:
    count = 0
    for a, val in enumerate(grades):
        if(val == grade):
            count = count + 1
    #appending the number of times a grade appears in list
    frequency.append(count)
#output
print("Grades = ",grades)
print("Frequency = ",frequency)

#QUESTION 3
print("\n\nAnswers of Question 3\n")
#A
dog_breeds = ['collie','sheepdog','chow','chihuahua']

#B
herding_dogs = dog_breeds[:2]

#C
tiny_dogs = [dog_breeds[-1]]

#D
check = 'Persian' in dog_breeds

#output
print("dog_breeds = ",dog_breeds)
print("herding_dogs = ",herding_dogs)
print("tiny_dogs = ",tiny_dogs)
print("check if 'Persian' in dog_breeds = ",check)
