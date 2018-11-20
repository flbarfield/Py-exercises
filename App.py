###### First Section, Operators ######

# Exercise:

# first = int(input("Please input three numbers to be multiplied. \nFirst number: "));
# second = int(input("Second Number: "));
# third = int(input("Third Number: "));
#
# while True:
#     first;
#     second;
#     third;
#     finalNum = first * second * third;
#     print("Your numbers multiplied is: ", finalNum);
#     break



##### Second Section, High Level Data Structures #####

##NOTES##
# dir returns all methods valid for the data type! Excellent for when you get stuck with a particular object type
# SLICING: var[a:b:c]... a = starting place. b = many element it'll count, c = how elements are incremented

# Excercises

#1
# Find the number of occurances of 1 in the list [1,2,1,2,1,2,3,4,1,2,3].

# givenList = [1,2,1,2,1,2,3,4,1,2,3]
# count = 0
#
# for i in givenList:
#     if i == 1:
#         count += 1
# print("There are ", count, " ones in this list.");

#2
# Find all the unique elements of a list. Input; a = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]. Output; [1, 2, 3, 4].
#
# """givenList2 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
# newlist = []
#
# for i in givenList2:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)
# """

#3
# Solve the above problem using a dictionary.

# givenList2 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
# storedDict = {}
# count = 0
# storedList = []
#
# for i in givenList2:
#     if i not in storedList:
#         storedList.append(i)
# storedDict['Number List is '] = storedList
# print(storedDict)

#4
# Find the count of each element of a list except "\n". a = [1, 2, 2, 3] should return this output. 1 : 1,, 2 : 2, 3 : 1.

# givenList2 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]
# storedDict = {}
#
# for i in givenList2:
#     if i not in storedDict.keys():
#         storedDict[i] = 1
#     else:
#         storedDict[i] += 1
# print(storedDict)

#5
# Create a random dictionary and print key : value pair in ascending order of keys. Input: a = {"IN":"India", "ES":"Español"}, output: "ES"":"Español", "IN":"India". You have to use dir to find out the necessary functions.

# randoDict = {'AZ' : 'Arizona', 'TX' : 'Texas', 'UT' : 'Utah', 'MS' : 'Mississippi'}
# print(sorted(randoDict))

#6
# The same example as above, print in descending order.

# randoDict = {'AZ' : 'Arizona', 'TX' : 'Texas', 'UT' : 'Utah', 'MS' : 'Mississippi'}
# print(sorted(randoDict, reverse=True))

#7 Given twos list, find their
# a) common elements.
# b) elements present in list a but not in b.
# c) elements present in list b but not in a. hint: use sets.

# -----A-----

"""SAME LISTS FOR A, B, C"""

# aList = ['apple', 'annie', 'bill', 'bob', 'joe']
# bList = ['Savannah', 'apple', 'billy', 'bob', 'jackson']
# newList = []

# for i in aList:
#     if i in bList:
#         newList.append(i)
# print(newList)

# -----B-----

# for i in aList:
#     if i not in bList:
#         newList.append(i)
# print(newList)

# -----C-----
# for i in bList:
#     if i not in aList:
#         newList.append(i)
# print(newList)

#8 Print a reverse of a list without using the reverse method.

# aList = ['apple', 'annie', 'bill', 'bob', 'joe']
#
# print(aList[::-1])

"""##### Third Section, Constructs #####"""


# 1 - Given that a = [1,2,3,4,[5,6,7]]
# Delete the first value.

# a = [1,2,3,4,[5,6,7]]

# del a[0]
# print(a)

# Delete the second value of the list present at index 4.

# del a[4]
# print(a)

# Delete the variable a.

# del a

# Take an input value from the user and delete it (if it is present), print "value not present" if the value is not present in the list.

# phraseList = []
# storedVar = input('Hey, Type anything. But type Q to quit: ')
#
# while True:
#     if 'Q' in storedVar:
#         break
#     elif storedVar in phraseList:
#         print("Hey! You've already typed that! But here's your current list.\n", phraseList)
#         storedVar = input('Try another again! Or enter "Q" to quit!: ')
#     else:
#         phraseList.append(storedVar)
#         print("Here's your current list: ", phraseList)
#         storedVar = input("Try more characters!: ")

#2
# Given that

# a = {"IN":"India", "ES":"Espanol"}

# Delete the key "IN".

# del a['IN']
# print(a)

# Delete the key "ES"
# del a['ES']

# Delete the variable a.
# del a

"""######## -- More Exercises -- #########"""

# 1
# Take the name, age and score of the user as input. Print their percentage. If the percentage is less than 60, print F, if percentage is between 60 and 70 print B and if percentage is greater than 70 print A. Marks are out of 100.

# score = int(input('What was your test score? : '))
#
# if score < 60:
#     print('YOU FAIL. LOL')
# elif score >= 60 and score < 70:
#     print('Ya get a B. Grats.')
# else:
#     print('YOU GOT AN A! YAHOO!')

#2 Take a number from the user and print if it is even or odd.

# storedNum = int(input('Input a number : '))
#
# if storedNum % 2 != 0:
#   print('Your number is odd')
# else:
#   print('Your number is even')

#3 Take two numbers from the user and print which number is largest.

# a = int(input('Please type a number : '))
# b = int(input('Please type another number : '))
#
# if a > b:
#     print(a, ' is the larger number.')
# elif a < b:
#     print(b, ' is the larger number.')
# elif a == b:
#     print('Both of your numbers are equal.')

#4 Take two numbers from the user and print which number is smallest.

# a = int(input('Please type a number : '))
# b = int(input('Please type another number : '))
#
# if a < b:
#     print(a, ' is the smaller number.')
# elif a > b:
#     print(b, ' is the smaller number.')
# elif a == b:
#     print('Both of your numbers are equal.')

#5 Take three numbers from the user and print largest and smallest number.

# numList = list(input('Please type a number sequence, no spaces'))
#
# print(numList)
#
# numList.sort()
#
# print(numList[::-1])

#6 Take four numbers from the user and create a list.

# numList = list(input('Please type a number sequence, no spaces'))
#
# print('Your number list is', numList)


#7 Take four numbers from the user and create a set.

# fillSet = set()
#
# numList = list(input('Please type a number sequence, no spaces'))
#
# print('Your number list is', numList)
#
#
# for i in numList:
#     fillSet.update(i)
# print('Your list is now a set: ', fillSet, "\nType: ", type(fillSet))



""" ####### Loop Exercises: ##########"""

#1
# Print all numbers till 100.

# val = [101]
# count = 0
#
# while count < 101:
#     if count != val:
#         print(count)
#         count += 1
#     else:
#         break

#2 Print all numbers from 20 to 100.

# val = [100]
# count = 0
#
# while count < 100:
#     if count != val:
#         count += 1
#         if count > 19:
#             print(count)
#     else:
#         break

#3 Print all even numbers less than 100.

# val = [100]
# count = 0
#
# while count < 100:
#     if count != val:
#         count += 1
#         if count % 2 == 0:
#             print(count)
#     else:
#         break

#4 Print all odd numbers less than 100.

# val = [100]
# count = 0
#
# while count < 100:
#     if count != val:
#         count += 1
#         if count % 2 != 0:
#             print(count)
#     else:
#         break

"""########## Exercises: Continue #########"""

#1 Print all numbers from 0 till 10 except 4 and 5.

# for i in range(11):
#     if i == 4 or i == 5:
#         continue
#     else:
#         print(i)

#2 Print all numbers from 0 till 20 except those divisible by 3.

# for i in range(21):
#     if i % 3 == 0:
#         print(i)
#     else:
#         continue

#3 a = [1,2,3,4,5], take an integer as input from the user. Print all numbers which are less than the input number using break.

# a = [1,2,3,4,5]
#
# storedInt = int(input('Please type a number 1-5 : '))
# newList = []
#
# for i in a:
#     if i < storedInt:
#         newList.append(i)
# print('Everything less than the number you typed is:\n', newList)

# Alternative...

# for i in a:
#     if i < storedInt:
#         print(i)

##### Exercises: While ######

#1
# Print all numbers till 100 using while.
#
# i = 0
#
# while i < 101:
#     print (i)
#     i += 1

#2 Print all numbers from 100 to 1 using while.

# i = 100
#
# while i > 0:
#     print (i)
#     i -=1

#3 Print all even numbers less than 100 using while.

# i = 100
#
# while i > 0:
#     if i % 2 == 0:
#         print(i)
#         i -= 1
#     else:
#         i -= 1
#         continue

#4 Print all odd numbers less than 100 using while.





# For a list [1,2,3,4,5], write a program which checks if 6 is present in the list, using while.

# Print all numbers from 0 to 10 except 4 and 5.
