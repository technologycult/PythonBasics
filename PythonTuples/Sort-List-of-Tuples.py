"""
Normal Order and Reverse Order Sort
1. Sort List of Tuples based on the First Element
2. Sort List of Tuples based on the Second Element
3. Sort List of Tuples based on the Last Element
"""

# movie_list_of_tuples = [
#                 ('Titanic',1997),('Matrix',1999),
#                 ('Skyfall',2012),('Joker',2019),
#                 ('MissionImpossible',1996),
#                 ('ShawshankRedemption',1994)]

# print('My Oringal Tuple is :', movie_list_of_tuples, '\n')

# # movie_list_of_tuples.sort()
# # print('Sorted list of Tuple based on the First Element :', movie_list_of_tuples, '\n')

# # movie_list_of_tuples.sort(reverse=True)
# # print('Sorted list of Tuple based on the First Element in Reverse Order:', movie_list_of_tuples, '\n')

# movie_list_of_tuples.sort(key = lambda item:item[1])
# print('Sorted list of Tuple based on the Second Element :', movie_list_of_tuples, '\n')

# movie_list_of_tuples.sort(key = lambda item:item[1], reverse=True)
# print('Sorted list of Tuple based on the Second Element in reverse order :', movie_list_of_tuples, '\n')


movie_list_of_tuples = [
                ('Titanic',1997,1800),('Matrix',1999,900),
                ('Skyfall',2012,1100),('Joker',2019,600),
                ('MissionImpossible',1996,500),
                ('ShawshankRedemption',1994,200)]

print('My Oringal Tuple is :', movie_list_of_tuples, '\n')

# movie_list_of_tuples.sort(key = lambda item:item[2])
# print('Sorted list of Tuple based on the Last Element :', movie_list_of_tuples, '\n')

# movie_list_of_tuples.sort(key = lambda item:item[2], reverse=True)
# print('Sorted list of Tuple based on the Last Element in revere order :', movie_list_of_tuples, '\n')



movie_list_of_tuples.sort(key = lambda item:item[-1])
print('Sorted list of Tuple based on the Last Element :', movie_list_of_tuples, '\n')

movie_list_of_tuples.sort(key = lambda item:item[-1], reverse=True)
print('Sorted list of Tuple based on the Last Element in revere order :', movie_list_of_tuples, '\n')




