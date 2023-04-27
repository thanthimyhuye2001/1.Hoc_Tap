# Thân Thị Mỹ Huyền - 20206288
# Thuật toán trên cấu trúc dữ liệu mảng
# Cho mảng a, số nguyên M. Tìm 1 mảng con sao cho tổng các phần tử bằng M

# Khai báo sử dụng thư viện Numpy
from numpy import *

# input mảng 
a = loadtxt('input.txt', dtype=float)
print('Mảng đã cho:\n',a)

#===============================================================
# Lưu vị trí các số không dương trong dãy a vào mảng index
# Nếu số đầu dương thì phần tử đầu tiên là -1
# Nếu số cuối dương thì phần tử cuối cùng là n

# n là số phần tử trong mảng
n = len(a)

index = []
if a[0] > 0:
    index.append(-1) 
    
for i in range(n):
    if a[i] <= 0:
        index.append(i)

if a[n-1] > 0:
    index.append(n)        

#===============================================================
# Tính tổng từng dãy con toàn dương
# Tìm dãy có tổng lớn nhất

MaxSum = 0
for i in range (len(index)-1):
    sum = 0
    for j in range (index[i]+1, index[i+1]):
        sum += a[j]
    
    print()    
    print(f'dãy {i+1}: {a[index[i]+1: index[i+1]]}')
    print(f'sum{i+1} = {sum}')
    
    if sum > MaxSum:
        MaxSum = sum
        start = index[i]+1
        finish = index[i+1] - 1         

# In ra dãy con toàn dương có tổng lớn nhất
print()
print(f'Dãy con toàn dương có tổng lớn nhất là:\n{a[start:finish+1]} \nCó tổng = {MaxSum}')       