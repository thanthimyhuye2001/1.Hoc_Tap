# Thân Thị Mỹ Huyền - 20206288
# Làm việc với mảng
# Liệt kê các số có số lần xuất hiện nhiều nhất trong mảng

from numpy import *
import numpy as np

# input mảng 
arr = [0, 9, 7, 2, 4, 9, 0, 4, 7, 4, 6, 1, 0]
print ('mảng: ',arr)
length = len(arr)

#---------------------------------------------------------------------
# ĐẾM số lần xuất hiện mỗi phần tử
# tạo mảng ĐẾM số lần xuất hiện của mỗi phần tử với giá trị ban đầu = 1
dem = np.ones_like(np.zeros(length)) 

# so sánh mỗi số với tất cả các phần tử đằng sau nó
# nếu bằng nhau thì tăng giá trị của biến "đếm" lên 1 đơn vị
for i in range(length):
    for j in range(i+1,length):
        if arr[i] == arr[j]:    
            dem[i] +=1    

#-------------------------------------------------
# xác định số lần xuất hiện lớn nhất 
max = dem[0]
for i in range(length):
    if max < dem[i]:
            max = dem[i]

#-------------------------------------------------
# in ra các phần tử xuất hiện nhiều nhất
print('Các phần tử xuất hiện nhiều nhất:')
for i in range(length):
    if dem[i] == max:
        print(arr[i]) 