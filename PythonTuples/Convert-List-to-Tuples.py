"""
Topic to be covered
How to Convert Python List to Tuples?
Method 1 - using tuple() builtin function
Method 2 - using loop inside tuple
Method 3 - using(*list,)
           unpacking the list inside the parenthesis

"""

movies_list = ['Titanic','Matrix',
               'Skyfall','Joker',
               'Mission Impossible',
               'Jumanji','Forest Gump']
                
print(type(movies_list))
print('The original list is :', movies_list, '\n')

# Method 1
# movies_tuples_1 = tuple(movies_list)
# print(type(movies_tuples_1))
# print('Convert from List to Tuple using inbuild tuple function :', movies_tuples_1)

# Method 2
# movies_tuples_2 = tuple(i for i in movies_list)
# print(type(movies_tuples_2))
# print('Convert from List to Tuple using loops :', movies_tuples_2)

# Method 3
movies_tuples_3 = (*movies_list,)
print(type(movies_tuples_3))
print('Convert from List to Tuple using unpacking :', movies_tuples_3)
















