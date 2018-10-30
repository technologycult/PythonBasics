"""
Python Basics - Session # 4

Topic to be covered - List in Python

"""

list1 = [1,2,3,4,'Hi','Hello','Bye',3.14,33.6,True]

list1 = [1,2,3,4,'Hi','Hello','Bye',3.14,33.6,True,[4,5,6]]

#How to reference a List
list1[6]

list1[-1][0]

# Slicing in Python List
# list [ number : n - 1]

list1[ 3 : 8 ]
list1[ 3 : 7 ]

# How to get the index of a partticular element

list1.index('Bye')
list1.index(3)

# Count the items
len(list1)

###############################################################################

tuple1 = (1,2,3,4)

list2 = [1,2,3,4,'Hi','Hello','Bye',3.14,33.6,True,[4,5,6],(1,2,3,4)]


lista = [1,2,3]
listb = ['a','b','c']

listc = [1,2,3]
listd = ['a','b','c']

listc = lista + listb

print(listc)

###############################################################################

# Change the list

listc[4] = 'x'

###############################################################################

# Difference between Append and Extend in List

lista.append(listb)
print(lista)

listc.extend(listd)
print(listc)

###############################################################################

# Delete operations in List

del listc[1]

listc.remove('a')

###############################################################################

# Aliasing in Python 

x = ['A','B','C']
y = x

x.extend('D')

###############################################################################

z = x[:]

x.append('E')


###############################################################################

lists = [8,7,5,4,3,2,10,0,1]
lists.sort()

list_string=['Venkat','Maneesh','Majid','Shwetha','Sonali','Mohsin']
list_string.sort() 
print(list_string)













































































