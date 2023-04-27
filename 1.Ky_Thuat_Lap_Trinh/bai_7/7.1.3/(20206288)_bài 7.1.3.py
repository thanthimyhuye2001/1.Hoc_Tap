# Thân Thị Mỹ Huyền - 20206288
# Thuật toán trên cấu trúc dữ liệu mảng
# Cho mảng a, số nguyên M. Tìm 1 mảng con sao cho tổng các phần tử bằng M

# Khai báo sử dụng thư viện Numpy
from numpy import *

# input mảng 
a = loadtxt('input.txt', dtype=float)
print('Cho mảng a:',a)
# n là số phần tử trong mảng
n = len(a)

M = int(input('Nhập tổng của dãy con: M = '))

# Tính tổng từng dãy con
for i in range (n):
    sum = 0
    
    for j in range (i, n):
        sum += a[j]
        
        # Ngắt vòng lặp của j khi tìm được dãy có tổng = M
        if (sum == M):              
            break
    
    # Ngắt vòng lặp của i khi tìm được dãy có tổng = M    
    if (sum == M):
        break   

if (sum == M):
    print(f'Dãy con có tổng bằng {M} là: {a[i: j+1]}')     
else:
    print('Không tìm được dãy con có tổng bằng M!')   
