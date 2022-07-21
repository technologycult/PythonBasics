"""
Topic to be covered - Subscript and Superscript

1. Negative Power
2. More than 1 digit number/value

No Superscript available for 
Small Letter - q but we can use letter ᑫ ('\u146b') as a workaround
Capital Letter - Q, S, X, Y , Z

No Subscript availabe for 
Small Letter - b,c,d,f,g,q,w,z
Capital Letter - Not Available
"""

dict1 = {'0':'\u2070','1':'\u00b9','2':'\u00b2',
         '3':'\u00b3','4':'\u2074','5':'\u2075',         
         '6':'\u2076','7':'\u2077','8':'\u2078',
         '9':'\u2079','+':'\u207A','-':'\u207B',
         '=':'\u207C','(':'\u207D',')':'\u207E',
         'a':'\u1d43','b':'\u1d47','c':'\u1D9C',
         'd':'\u1d48','e':'\u1d49','f':'\u1da0',
         'g':'\u1d4d','h':'\u02b0','i':'\u2071',
         'j':'\u02b2','k':'\u1d4f','l':'\u02e1',
         'm':'\u1d50','n':'\u207f','o':'\u1d52',
         'p':'\u1d56','r':'\u02b3','s':'\u02e2',
         't':'\u1d57','u':'\u1d58','v':'\u1d5b',
         'w':'\u02b7','x':'\u02e3','y':'\u02b8',
         'z':'\u1dbb','A':'\u1D2c','B':'\u1D2E',
         'D':'\u1d30','E':'\u1d31','G':'\u1d33',
         'H':'\u1d34','I':'\u1d35','J':'\u1d36',
         'K':'\u1d37','L':'\u1d38','M':'\u1d39',
         'N':'\u1d3a','O':'\u1d3c','P':'\u1d3e',
         'R':'\u1d3f','T':'\u1d40','U':'\u1d41',
         'V':'\u2c7d','W':'\u1d42','q':'\u146b'
         }

dict2 = {'0':'\u2080','1':'\u2081','2':'\u2082',
         '3':'\u2083','4':'\u2084','5':'\u2085',
         '6':'\u2086','7':'\u2087','8':'\u2088',
         '9':'\u2089','+':'\u208A','-':'\u208B',
         '=':'\u208C','(':'\u208D',')':'\u208E',
         'a':'\u2090','e':'\u2091','h':'\u2095',
         'i':'\u1d62','j':'\u2c7c','k':'\u2096',
         'l':'\u2097','m':'\u2098','n':'\u2099',
         'o':'\u2092','p':'\u209A','r':'\u1d63',
         's':'\u209B','t':'\u209C','u':'\u1d64',
         'v':'\u1d65','x':'\u2093','y':'\u1d67'     
         }

def sups(base,x):
    z = '{}'.format(dict1.get(x))
    return base + z

def subs(base,x):
    z = '{}'.format(dict2.get(x))
    return base + z 

def supscript(base,x,p):
    y = ''
    for i in x:
        z = '{}'.format(dict1.get(i))
        y = y + z
        print(y)
    return sups(base,p) + y

def subscript(base,x,p):
    y = ''
    for i in x:
        z = '{}'.format(dict2.get(i))
        y = y + z
        print(y)
    return subs(base,p) + y

        











    



