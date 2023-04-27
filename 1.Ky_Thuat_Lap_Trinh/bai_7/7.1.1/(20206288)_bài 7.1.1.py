# Thân Thị Mỹ Huyền - 20206288
# Thuật toán trên cấu trúc dữ liệu mảng
# Tính khoảng cách trung bình giữa các giá trị trong mảng
 
# Khai báo sử dụng thư viện Numpy
from numpy import *

# input mảng 
arr = loadtxt('input.txt', dtype='float')
print('Mảng đã cho:',arr)

# n là số phần tử trong mảng
n = len(arr)

sum = 0
dem = 0
for i in range (n-1):
    for j in range (i+1, n):     
        KhoangCach = abs(arr[i] - arr[j])
        sum += KhoangCach
        dem += 1  

KhoangCachTB = sum / dem
print('Khoảng cách trung bình giữa các giá trị trong mảng: ',KhoangCachTB)
