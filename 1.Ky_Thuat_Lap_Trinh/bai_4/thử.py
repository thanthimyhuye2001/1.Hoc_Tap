from numpy import *
import numpy as np
# input 2 ma trận 
matrix1 = np.loadtxt('C:/Users/HAN NGA/Downloads/Học Python/Kỹ Thuật lập trình/bài 4/matran A.txt', dtype=float)
print ('Ma trận 1\n',matrix1)
n = len(matrix1)

E = eye(n)
print(E)