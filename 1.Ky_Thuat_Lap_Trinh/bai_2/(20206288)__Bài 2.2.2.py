'''
Thân Thị Mỹ Huyền - 20206288
Viết chương trình kiểm tra một số có phải số nguyên tố hay không '''

from math import *

n = int(input("nhập số tự nhiên n = "))
if n < 0:
    print("ERROR")
elif n < 2:
    print("không là số nguyên tố")
else:
    dem = 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            dem += 1
    
    if (dem == 0): 
        print("là số nguyên tố")   
    else: 
        print("không là số nguyên tố")           
