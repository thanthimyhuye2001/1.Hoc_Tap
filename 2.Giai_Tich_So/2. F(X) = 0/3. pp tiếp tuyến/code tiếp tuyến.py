from hashlib import sha3_224
from math import *

# input
ep = float(input('nhập vào sai số epsilon = '))
print('nhập khoảng cách ly nghiệm (a,b)')
a = float(input('a = '))
b = float(input('b = '))
dem = 0

def f(x):                    # định nghĩa hàm f(x)
    return log(x)-1

f_a = f(a)                   
f_b = f(b)

def dx_f(x0):                # đạo hàm f'(x)
    return (f(x0+0.00001)-f(x0-0.00001))/(2*0.00001)
# tính ep0 để thiết lập điều kiện dừng
dx_fa = dx_f(a)
dx_fb = dx_f(b)
if abs(dx_fa) >= abs(dx_fb): 
    min = abs(dx_fb)
else:
    min = abs(dx_fa)     

def dx_dx_f(x00):            # đạo hàm f''(x)
    return (dx_f(x00+0.00001)-dx_f(x00-0.00001))/(2*0.00001)

dx_dx_fa = dx_dx_f(a)
dx_dx_fb = dx_dx_f(b)
if abs(dx_dx_fa) > abs(dx_dx_fb):
    Max = abs(dx_dx_fa)
else:
    Max = abs(dx_dx_fb)    

ep0 = sqrt(ep*2*min/Max)      # tính epsilon0 để thiết lập điều kiện dừng

S1 = f_a * f_b
S2 = dx_fa * dx_fb
S3 = dx_dx_fa*dx_dx_fb
if( S1 < 0 and S2 > 0 and S3 > 0):   # kiểm tra xác định dấu không đổi  S3 và S2 > 0
    if f_a*dx_dx_fa > 0:             # tìm điểm Furier để tiết tuyến tại đó cắt Ox
        x0 = a
    else:
        x0 = b
        
    f_x0   = f(x0)    
    dx_fx0 = dx_f(x0)                 
    dx     = f_x0/dx_fx0       # tính delta = x(k+1) - x(k)
    
    while abs(dx) > ep0:       # vòng lặp
        x0 -= dx
        f_x0 = f(x0)
        dx_fx0 = dx_f(x0)
        dx     = f_x0/dx_fx0   
        dem +=1
        print(x0)
        
    print('nghiệm x = ',x0,'\nsố lần lặp = ', dem)  
    
elif (S1==0):
    if a==0: print('nghiệm x = ',a)  
    if b==0: print('nghiệm x = ',b)   
     
else:
    print("Khoảng cách ly không hợp lệ, không tồn tại nghiệm duy nhất")
