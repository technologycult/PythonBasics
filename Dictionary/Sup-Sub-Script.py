"""
Topic to be covered - Subscript and Superscript
"""

dict1 = {'0':'\u2070',
         '1':'\u00b9',
         '2':'\u00b2',
         '3':'\u00b3',
         '4':'\u2074',
         '5':'\u2075',
         '6':'\u2076',
         '7':'\u2077',
         '8':'\u2078',
         '9':'\u2079',
         '+':'\u207A',
         '-':'\u207B',
         '=':'\u207C',
         '(':'\u207D',
         ')':'\u207E',
         'n':'\u2084',}

dict2 = {'0':'\u2080',
         '1':'\u2081',
         '2':'\u2082',
         '3':'\u2083',
         '4':'\u2084',
         '5':'\u2085',
         '6':'\u2086',
         '7':'\u2087',
         '8':'\u2088',
         '9':'\u2089',
         '+':'\u208A',
         '-':'\u208B',
         '=':'\u208C',
         '(':'\u208D',
         ')':'\u208E',
         'a':'\u2090',
         'e':'\u2091',
         'o':'\u2092',
         'x':'\u2093',
         'h':'\u2095',
         'k':'\u2096',
         'l':'\u2097',
         'm':'\u2098',
         'n':'\u2099',
         'p':'\u209A',
         's':'\u209B',
         't':'\u209C'}

def sups(base,x):
    z = '{}'.format(dict1.get(x))
    return base + z

def subs(base,x):
    z = '{}'.format(dict2.get(x))
    return base + z






















'''
 # Task No 1 - y² = 4ax
 
print(sups('y','2') + ' = 4ax')

# Task No 2 - x²/a² + y²/b² = 1
print(sups('x','2') + '/' + sups('a','2') + ' + ' + 
      sups('y','2') + '/' + sups('b','2') + ' = 1')


# Task No 3  
# H₂SO₄
print(subs('H','2') + subs('SO','4'))


# Task No 4
# CaCl2
print(subs('CaCl','2'))

# Task No 5
# H₂SO₄ + CaCl₂ = HCl + CaSO₄
print(subs('H','2') + subs('SO','4') + ' + ' + 
      subs('CaCl','2') + ' = ' + 
      'HCl' + ' + ' + 
      subs('CaSO','4'))
'''

























    
    
    
    
    
    
