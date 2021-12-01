"""
Topics to be covered :
How to convert Python Tuples to Dictionaries?
1. Python dict() method
2. Python zip() method
"""

tuple1 = (('Titanic',1997),
          ('Skyfall',2012),
          ('Joker',2019),
          ('ForestGump',1994),
          ('Lagaan',2001))

dct1 = dict(tuple1)
print(type(dct1))
print('The dictionary is : \n', dct1)





movies_tuple = ('Titanic','Matrix',
                'Skyfall','Joker',
                'ForestGump','Lagaan')

year_tuple = (1997,1999,2012,2019,1994,2001)

dct2 = dict(zip(movies_tuple, year_tuple))
print(type(dct2))
print('Dictionary is : \n', dct2)














