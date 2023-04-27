from math import *
# nhập dl đầu vào
def input_data():
    ep = float(input('nhập vào sai số epsilon = '))
    print('nhập khoảng cách ly nghiệm (a,b)')
    a = float(input('a = '))
    b = float(input('b = '))
    return ep,a,b

def f(x):                    # định nghĩa hàm f(x)
    return log(x)-1
def find_x(ep,a,b):          #hàm tìm giá trị x = c
    if f(a) > 0: sig = 1     # B1: xác định dấu của f(a)
    else: sig = -1
    c=(a+b)/2                # B2: tìm điểm giữa
    z=f(c)
    if z==0: return c
    
    while f(c) != 0:        # thực hiện vòng lặp
        print(f(c))
        if z*sig < 0: b = c  # vì f(a) f(b) trái dấu
        else: a = c
        if abs(a-b)< ep : return c
        c = (a+b)/2
        z = f(c)
    return c
def main():
    ep,a,b = input_data()
    print('nghiệm x = ',find_x)      
main()    