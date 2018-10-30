'''

Python Basics - Session # 5 

Topic to be covered - Tuples in Python


1. What is Tuples
2. Creating Tuples
3. Accessing Tuples elements
4. Updating Tuples
5. Tuples Concatenation
6. Tuples Nesting
7. Delete Tuples
8. Multiply/Repetition in Tuples
9. Slicing in Tuples
10. How to find the length of a Tuple
11. How to convert List into a Tuple
12. Iterations in Tuples
13. Tuple Functions 
14. Difference between Tuples and List
'''

#1. What is Tuples

'''
1. Tuples is a collection of mix data type/objects seperated by comma.
2. It is ordered.
3. They are Immutable (cannot be changed / modified).
4. Tuples is created using round bracked whereas Lists are created using
   Square Bracket.
'''

#2. Creating Tuples

tuple1 = ('India')
print(type(tuple1))


tuple2  = ('India',)
print(type(tuple2))


#3. Accessing Tuples elements

mytuple = ('India','China','Russia','Germany','Japan','USA','UK')

mytuple[0]

mytuple[2]

mytuple[-1]

#4. Updating Tuples

mytuple[1] = 'Sweden'

mylist = ['India','China','Russia','Germany','Japan','USA','UK']
mylist.append('Sweden')

#5. Tuples Concatenation
mytuple1 = ('Sweden','France','Ireland')

tuple_concat = mytuple + mytuple1
print(tuple_concat)


#6. Tuples Nesting
tuplea = (1,10,34,500,600,3.14)
tupleb = ('Ajay','Akshay','Amir','Arun')

tuplec = (tupla,tupleb)
print(tuplec)

 
#7. Delete Tuples

del tuplec


#8. Multiply/Repetition in Tuples

tuple_repet = ('Jai','ho','India')
print(tuple_repet * 5)

#9. Slicing in Tuples
print(mytuple)
print(mytuple[1:3])
print(mytuple[2:5])


#10. How to find the length of a Tuple
print(len(mytuple))

#11. How to convert List into a Tuple
tuple_from_list = tuple(mylist)
print(tuple_from_list)

#12. Iterations in Tuples
for i in range(len(mytuple)):
    print(mytuple[i])

#13. Tuple Functions 


# Max
print(max(tuplea))

print(min(tuplea))



#14. Difference between Tuples and List
'''
1. Round bracket and Square bracket 
2. Tuples are immutable where as Lists can be changed
3. Execution time is less in case of tuple
4. Tuple can be dictionary Keys wheres List cannot be.
5. Tuple can be a value in set whereas List cannot be.
'''


import timeit

print(timeit.timeit('x=(1,2,3,4,5)', number=10000000))
print(timeit.timeit('x=[1,2,3,4,5]', number=10000000))

















