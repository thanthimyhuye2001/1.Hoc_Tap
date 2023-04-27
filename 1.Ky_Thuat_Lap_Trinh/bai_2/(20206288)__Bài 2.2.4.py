'''
Thân Thị Mỹ Huyền - 20206288
Tìm ước số chung lớn nhất, bội số chung nhỏ nhất của hai số nhập từ màn hình'''

a = int(input('nhập số tự nhiên thứ 1 = '))
b = int(input('nhập số tự nhiên thứ 2 = '))

if (a < 0 or b < 0):
    print("ERROR")
    
elif (a == 0 or b == 0):
    if (b != 0):
        print("Uớc số chung lớn nhất: ",b)
    if (a != 0): 
        print("Uớc số chung lớn nhất: ",a)
    if (a == b): 
        print("cặp (0, 0) không có ước số chung lớn nhất")
        
    print("Bội số chung nhỏ nhất: ",0)
    
else:
    S = a*b
    while a != b :
        if (a > b): a = a - b
        else: b = b - a
        
    print("Uớc số chung lớn nhất: ",a)
    print("Bội số chung nhỏ nhất: ",S/a)    