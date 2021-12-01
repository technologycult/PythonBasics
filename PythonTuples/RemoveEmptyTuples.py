"""
Topics to be covered :
How to remove empty tuple from list of tuples
Method # 1
List Comprehension
Method # 2
Filter Method
"""

movies_list_of_tuples = [('Titanic',1997),
                         ('Matrix',1999),
                         (),
                         ('Skyfall',2012),
                         ('Joker',2019),
                         ('MissionImpossible',1996),
                         ('ShawshankRedemption',1994),
                         ()]

print('Tuple is \n',movies_list_of_tuples)

# Method No 1 - using List Comprehension
# movies_remove_dups = [tup for tup in movies_list_of_tuples if tup]
# print(movies_remove_dups)

# Method No 2 - Using Filter method
movies_remove_empty = filter(None,movies_list_of_tuples)
print(type(movies_remove_empty))
print(movies_remove_empty)

list1 = []
for i in movies_remove_empty:
    print(i)
    list1.append(i)

print('The list after removing the empty tuples :', list1)

# print('After first for Loop')
# for i in movies_remove_empty:
#     print(i)

























































