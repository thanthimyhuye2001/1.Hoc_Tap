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
S1 = f_a * f_b

def dx_f(x0):                # đạo hàm f'(x)
    return (f(x0+0.00001)-f(x0-0.00001))/(2*0.00001)
# tính ep0 để thiết lập điều kiện dừng
dx_fa = dx_f(a)
dx_fb = dx_f(b)
S2 = dx_fa * dx_fb

if abs(dx_fa) >= abs(dx_fb): 
    Max = abs(dx_fa)
    min = abs(dx_fb)
else:
    Max = abs(dx_fb)
    min = abs(dx_fa)     
ep0 = (ep*min)/(Max - min)

#kiểm tra xác định dấu không đổi  S3 và S2 > 0
def dx_dx_f(x):            # đạo hàm f''(x)
    return (dx_f(x+0.00001)-dx_f(x-0.00001))/(2*0.00001)
S3 = dx_dx_f(a)*dx_dx_f(b)

if( S1 < 0 and S2 >0 and S3>0):
    if f_a*dx_dx_f(a) > 0:
        d = a
        x0 = b
    else:
        d = b
        x0 = a
        
    f_x0 = f(x0)    
    f_d  = f(d)                  # bước 4
    dx   = f_x0*(d-x0)/(f_x0-f_d)
    
    while abs(dx) > ep0:
        x0 += dx
        f_x0 = f(x0)
        f_d = f(d)
        dx = f_x0*(d-x0)/(f_x0-f_d)
        dem +=1
        print(x0)
        
    print('nghiệm x = ',x0,'\nsố lần lặp = ', dem)  
    
elif (S1==0):
    if a==0: print('nghiệm x = ',a)  
    if b==0: print('nghiệm x = ',b)   
     
else:
    print("Khoảng cách ly không hợp lệ, không tồn tại nghiệm duy nhất")
