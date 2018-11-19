###### First Exercise ######
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



#####Second Section#####

##NOTES##
# dir returns all methods valid for the data type! Excellent for when you get stuck with a particular object type
# SLICING: var[a:b:c]... a = starting place. b = many element it'll count, c = how elements are incremented

# Excercises
"""
2.
3.
4.
5.
6.
7.
"""

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

randoDict = {'AZ' : 'Arizona', 'TX' : 'Texas', 'UT' : 'Utah', 'MS' : 'Mississippi'}
print(randoDict.get('AZ'))

#6
# The same example as above, print in descending order.

#7 Given twos list, find their
# a) common elements.
# b) elements present in list a but not in b.
# c) elements present in list b but not in a. hint: use sets.

#8 Print a reverse of a list without using the reverse method.
