# Thân Thị Mỹ Huyền - 20206288
# Thuật toán trên cấu trúc dữ liệu mảng
# Xóa các phần tử trùng nhau trong một mảng

# Khai báo sử dụng thư viện Numpy
from numpy import *

# input mảng 
arr = loadtxt('input.txt', dtype=str)
print('Mảng đã cho:')
print(arr)

# n là số phần tử trong mảng
n = len(arr)

# Tạo 1 mảng rỗng để lưu trữ các phần tử của mảng đã cho, sao cho không có phần tử nào trùng nhau
arrNew = []

# Phần tử nào chưa có trong arrNew sẽ được thêm vào arrNew
for i in range (n):
    Kiem_tra =  arr[i] not in arrNew
    if Kiem_tra == True:
        arrNew.append(arr[i])
        
print()      
print('Mảng sau khi xóa các phần tử trùng nhau:')
print(arrNew)  
print()      
        