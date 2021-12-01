""" 
Topic to be covered
Different ways to Concatenate Tuples
1. Using '+' Operator
2. Concatenate tuples using sum() function
3. Concatenate tuples inside a tuple
4. Concatenate tuples using map() function
5. Concatenate tuples using zip() function
6. Concatenate tuples inside a list
7. Concatenate tuples inside a list using join() function
8. Concatenate consecutive tuples
"""

movie_tuples = ('Titanic','Matrix',
                        'Skyfall','Joker',
                        'MissionImpossible',
                        'ShawshankRedemption')

release_year = (1997,1999,2012,2019,1196,1994)

release_year_1 = (1994,1996,1997,1999)
release_year_2 = (2000,2001,2006,2012,2021)

# Method 1
# concat_tuple = release_year_1 + release_year_2
# print('Concatenated Tuple is :', concat_tuple)

# Method 2
# concat_tuple = movie_tuples + release_year
# print('Concatenated Tuple is :', concat_tuple)

# Method 3 - using sum() function
# concat_tuple = sum((movie_tuples, release_year), ())
# print('Concatenated Tuple is :', concat_tuple)

# Method 4 - Concatenate tuples inside a tuple
# concat_tuple = (movie_tuples, release_year)
# print('Concatenated Tuple is :', concat_tuple)

# Method 5 - Concatenate tuples using map() function
# from operator import concat
# release_year = ('1997','1999','2012','2019','1996','1994')
# concat_tuple =   tuple(map(concat,movie_tuples,release_year))
# print('Concatenated Tuple is :', concat_tuple)

# Method 6 - Concatenate tuples using zip() function
# concat_element_wise = tuple(zip(movie_tuples,release_year))
# print('Concatenated Tuple is :', concat_element_wise)

# Method 7 - Concatenate inside a list
# tuples_inside_list = [movie_tuples,release_year]
# print('Tuples inside list :', tuples_inside_list)

# Method 8 - Concatenate using Join() function
# release_year = ('1997','1999','2012','2019','1996','1994')
# tuples_inside_list = [movie_tuples,release_year]
# concat_via_join = [' '.join(tup) for tup in tuples_inside_list] 
# print('Concatenated tuple via Join is :', concat_via_join)

# Method 9 - Concatenate consecutive elements
output_tuple = tuple(i + j for i, j in zip(movie_tuples, movie_tuples[1:]))
print(output_tuple)










































































