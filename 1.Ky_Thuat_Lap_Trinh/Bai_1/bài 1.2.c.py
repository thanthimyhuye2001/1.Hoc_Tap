'''Thân Thị Mỹ Huyền - 20206288
   Giải phương trình bậc 2 với số thực và số phức'''

from math import *

print("giải phương trình bậc 2: ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
    if b == 0: 
        if c == 0:
            print('phương trình vô số nghiệm ')
        else:
            print('phương trình vô nghiệm ')    
    else:
        if (c==0):
            print('phương trình có 1 nghiệm x = 0')
        else:   
            print('phương trình có 1 nghiệm x = ',-c/b)
else:
    delta = b**2 - 4*a*c
    if (delta > 0):
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print('phương trình có 2 nghiệm: ',x1,'   ',x2)
    elif (delta == 0):
        print('phương trình có 1 nghiệm: ',-b/(2*a))
    else:
        re = -b/(2*a)
        im = sqrt(-delta)/fabs((2*a))
        print('phương trình có 2 nghiệm phức:',re,'+',im,'i   ',re,'-',im,'i')              