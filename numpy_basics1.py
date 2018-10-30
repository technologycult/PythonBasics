'''
Python Basics - Session # 6 

Topic to be covered - Numpy in Python


1. What is Numpy
2. Creating Numpy 
3. Accessing Numpy elements
4. Updating Numpy
5. Indexing / Slicing in Numpy
6. Basic Operations in Numpy
7. Functions using Numpy
   mean, max, min, sort, var, std, argmin, argmax, nonzero, where, extract, 
8. Broadcasting in Numpy 
9.  Numpy String Functions
10. Storage Comparision between List and Numpy
11. Processing time comparision between List and Numpy
12. Matrix / Linear Algebra using Numpy
13. Iterations with Numpy
14. Numpy - converting to hexadecimal
15. I/O with Numpy
16. Matplotlib with Numpy
    Various options to be explored
    Barplot
'''

###############################################################################
# 1. What is Numpy ?

'''
1. Numpy is a library for scientific computing.
2. Numpys stands for Numerical Python.
3. Numpy consists of Multidimensional array objects and it has collection of 
   functions/routines to process those arrays.
4. There are advantages of using Numpy
   a. Takes less memory as compared to List
   b. Processing speed of numpy array is much higher.
'''

###############################################################################
# 2. How do we create numpy array?

import numpy as np

x = np.array([1,2,3])
print(x)

print(x.dtype)

x = np.array([1,2,3.0])
print(x.dtype)
print(x)

x = np.array([10,20,30,40,50], ndmin = 3)
print(x)
print(x.size)
print(x.shape)


###############################################################################
# 3. Accessing Numpy Elements

x = np.array([10,20,30,40,50])
print(x[2])
print(x[-1])
print(x[-3])

###############################################################################
# 4. Updating Numpy array

print(x)
x[2] = 80
print(x)

###############################################################################
# 5. Indexing / Slicing in Numpy

# Type 1

x = np.arange(10)

s = slice(2,9,2)
print(x[s])
print(x[slice(0,8,2)])
print(x[slice(1,8,3)])

print(x[0:8:2])
print(x[1:8:3])

x = np.arange(20)
y = x[10]
print(y)

y = x[:10]
print(y)

y = x[10:]
print(y)

print(y[2:8])

print(y[2:10:2])
print(y[2:10:3])
#

x = np.array([[10,20,30], [40,50,60], [70,80,90]])
print(x) 
'''
[[10 20 30]   ----- 0
 [40 50 60]   ----- 1
 [70 80 90]]  ----- 2
'''


######
print(x[1:])
print(x[2:])
print(x[0:])
print(x[3:])

print(x[:,0])
print(x[:,1])
print(x[:,2])

###############################################################################
# 6. Basic Operations in Numpy


x = [10,20,30]
y = [30,60,70]

print(x + y)
print(y / 10)

x = np.array([10,20,30])
y = np.array([30,60,70])

print(x+y)
print( y / 10)

print ( x * 10)

###############################################################################
#7. Functions using Numpy
#   mean, max, min, sort, var, std, argmin, argmax, nonzero, where, extract, 

Sachin_runs = np.array([110,105,155,0,191,174,0])

print(np.mean(Sachin_runs))
print(np.min(Sachin_runs))
print(np.max(Sachin_runs))
print(np.var(Sachin_runs))
print(np.std(Sachin_runs))
print(np.argmax(Sachin_runs))
print(np.argmin(Sachin_runs))
print(np.nonzero(Sachin_runs))

print(np.where(Sachin_runs > 120))

condition = (Sachin_runs > 100) & (Sachin_runs < 160) 
print(np.extract(condition, Sachin_runs))

###############################################################################
# 8.  BroadCasting in Python

'''
The term broadcasting describes how numpy treats arrays with different shapes 
during arithmetic operations. Subject to certain constraints, the smaller array 
is “broadcast” across the larger array so that they have compatible shapes. 
'''

###############################################################################
# 9.  Numpy String Functions

''' add '''

u = 'hello'
v = ' world'

print(np.char.add(u,v))


print(np.char.multiply(u,3))

''' center '''
print(np.char.center(u,11,fillchar='#'))
                     
''' Capitalize '''
print(np.char.capitalize(u + v))

''' title '''

print(np.char.title(u + v))

''' lower & uppper '''
print(np.char.lower('HELLO'))
print(np.char.upper('world'))

'''split '''
print(np.char.split('my name is khan'))

'''splitlines'''
print(np.char.splitlines('my name is \n khan'))

''' replace '''

print(np.char.replace('dd//mm//yy','//',':'))

print(np.char.replace('My name is Oly','Oly','Aly'))

'''encode and decode'''


enc = np.char.encode('alpha',encoding='cp424')
print(enc)

dec =np.char.decode(enc, 'cp424')
print(dec)

###############################################################################
# 10. Storage comparision between List and Numpy
''' Storage Comparision '''

import sys

Size = range(1000)
print(sys.getsizeof(Size) * len(Size))

Nump = np.arange(1000)
print(Nump.size * Nump.itemsize)

###############################################################################
###############################################################################
# 11. Speed Comparision between List and Numpy

''' Speed Comparision '''

import time

size = 10000
t1 = time.time()

X = range(size)
Y = range(size)

Z = [ X[i] + Y[i] for i in range(len(X))]

print('Time taken by List :', time.time() - t1)

t2 = time.time()

X = np.arange(size)
Y = np.arange(size)

Z = X + Y

print('Time taken by Numpy Array :', time.time() - t2)

############################################################################

# 12. Matrix / Linear Algebra using Numpy

'''
There is a separate Playlist for Matrices / Vector and Linear Algenbra, 
So will not cover here
'''

###############################################################################

# 13. Iterations with Numpy

x = np.random.randint(0,9,(5,5))
print(x)
print(x.T)

for i in np.nditer(x):
    print(i)


y = np.arange(0,100,5)

print(y.T)


y1 = np.random.randint(0,9,(4,4))
print(y1)

print(y1.reshape(2,8))
print(y1.reshape(8,2))

###############################################################################

#14. Numpy Byte Swapping
    
    
###############################################################################
    
#15. I/O with Numpy



###############################################################################
"""
16. Matplotlib with Numpy
    Scatterplot and it various options to be explored
    Barplot
"""
