# Thân Thị Mỹ Huyền - 20206288
# Làm việc với mảng
# Thực hiện các phép toán của vector và ma trận (+,-, tích ) qua hàm
from numpy import *
import numpy as np

# input 2 ma trận 
matrix1 = np.loadtxt('C:/Users/HAN NGA/Downloads/Học Python/Kỹ Thuật lập trình/bài 4/matran A.txt', dtype=float)
print ('Ma trận 1\n',matrix1)

matrix2 = np.loadtxt('C:/Users/HAN NGA/Downloads/Học Python/Kỹ Thuật lập trình/bài 4/matran B.txt', dtype=float)
print ('\nMa trận 2\n',matrix2)

(hang1, cot1) = matrix1.shape
(hang2, cot2) = matrix2.shape

#-----------------------------------------------------------------
# Tổng hiệu 2 Ma trận
if (hang1, cot1) == (hang2, cot2):
    sum = add(matrix1, matrix2) 
    hieu = subtract(matrix1, matrix2)
    
    print('\nTổng 2 ma trận\n', sum)
    print('\nHiệu 2 ma trận\n', hieu)
    
else:
    print('\n2 ma trận không cùng kích cỡ không cộng trừ được')
    
#-----------------------------------------------------------------
# Tích 2 Ma trận
if cot1 == hang2:   
    tich = matrix1.dot(matrix2)
    print('\nTích 2 ma trận\n', tich)
else:
    print('\ncột ma trận 1 không bằng hàng ma trận 2 nên không nhân được')