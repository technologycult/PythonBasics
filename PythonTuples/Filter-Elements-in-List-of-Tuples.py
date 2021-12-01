"""
Topic to be covered
1. How to filter List of elements in List of Tuples?
"""

movie_list_of_tuples = [
                ('Titanic',1997),('Matrix',2019),
                ('Skyfall',2012),('Joker',2019),('Matrix',1999),
                ('MissionImpossible',1996),('Matrix',1999),
                ('ShawshankRedemption',1994),('Skyfall',2012),
                ('MissionImpossible',2001)]

print('My Oringal Tuple is : \n', movie_list_of_tuples, '\n')

filterterm = 2019

filter_output = list(filter(lambda x : filterterm in x, movie_list_of_tuples))
print(filter_output)