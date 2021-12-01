movie_tuples = [('Titanic',1997),('Matrix',1999),
                ('Skyfall',2012),('Joker',2019),
                ('MissionImpossible',1996),
                ('ShawshankRedemption',1994)]

print("My Original list of Tuple : \n", movie_tuples)

movie_tuples.sort()
print('Sorted list of tuples by movie name: \n', movie_tuples)

movie_tuples.sort(reverse=True)
print('Sorted list of tuples by movie name in Reverse Order: \n', movie_tuples)
# # #####################################################
# Sort by the year

movie_tuples.sort(key = lambda item:item[1])
print('Sorted list of tuples by year:\n', movie_tuples)

movie_tuples.sort(key = lambda item:item[1], reverse=True)
print('Sorted list of tuples by year in Reverse Order:\n', movie_tuples)