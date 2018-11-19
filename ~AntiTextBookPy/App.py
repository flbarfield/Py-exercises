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

##### Third Section, Constructs #####

# Exercises:

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

phraseList = []
storedVar = input('Hey, Type anything. But type Q to quit: ')

while True:
    if 'Q' in storedVar:
        break
    elif storedVar in phraseList:
        print("Hey! You've already typed that! But here's your current list.\n", phraseList)
        storedVar = input('Try another again! Or enter "Q" to quit!: ')
    else:
        phraseList.append(storedVar)
        print("Here's your current list: ", phraseList)
        storedVar = input("Try more characters!: ")
