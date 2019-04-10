'''
Python 3 Basics - Session # 10

Topic to be covered - if, if-else, if-elif-else
'''

number = 0

if number > 0:
    print('Positive Number')
print('This line will always be printed')

###############################################################################
number = int(input('Enter the number : '))

if number >= 0:
    print('Positive Number OR Zero')
else:
    print('Negative Number')

###############################################################################
    
number = int(input('Enter the number : '))

if number > 0:
    print('Positive Number')
elif number == 0:
    print('Zero')
else:
    print('Negative Number')

###############################################################################
    
side1 = int(input('Enter the side a : '))    
side2 = int(input('Enter the side b : '))
side3 = int(input('Enter the side c : '))

if ((side1 + side2 > side3) & (side2 + side3 > side1) & (side3 + side1 > side2)):
    print('Traingle can be formed')
    if ((side1 == side2) & (side2 == side3)):
        print('Traingle is Equilateral')
    elif ((side1 == side2) & (side2 != side3)):
        print('Isosceles Triangle')
    elif ((side2 == side3) & (side3 != side1)):
        print('Isosceles Triangle')
    elif ((side3 == side1) & (side1 != side2)):
        print('Isosceles Triangle')
    elif ((side1**2 + side2**2 == side3**2)):
        print('Right Angled Triangle')
    elif ((side1 != side2) & (side2 != side3)):
        print('Scalene Triangle')
    elif ((side2**2 + side3**2 == side1**2)):
        print('Right Angled Triangle')
    elif ((side3**2 + side1**2 == side1**2)):
        print('Right Angled Triangle')
else:
    print('Traingle cannot be formed with the given dimensions')















