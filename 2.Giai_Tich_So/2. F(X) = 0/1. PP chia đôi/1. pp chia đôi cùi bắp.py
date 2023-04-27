from math import *
# nhập dl đầu vào

ep = float(input('nhập vào sai số epsilon = '))
print('nhập khoảng cách ly nghiệm (a,b)')
a = float(input('a = '))
b = float(input('b = '))
dem = 0

f_a = log(a)-1
f_b = log(b)-1
S = f_a * f_b
if( S > 0): 
    print("Khoảng cách ly không hợp lệ, không tồn tại nghiệm duy nhất")
elif (S==0):
    if a==0: print('nghiệm x = ',a)  
    if b==0: print('nghiệm x = ',b)    
else:
    if f_a > 0: sig = 1     # B1: xác định dấu của f(a)
    else: sig = -1
    dem = 0
    while abs(a-b) > ep:  # kiểm tra điều kiện dừng
        c = (a+b)/2
        print(c)
        f_c = log(c)-1
        if f_c == 0: 
            break
        if f_c*sig < 0: 
            b = c          # vì giá trị tại khoảng cách ly trái dấu
            dem +=1
        else: 
            a = c
            dem +=1
        
    print('nghiệm x = ',c,'\n','số lần lặp = ', dem)  