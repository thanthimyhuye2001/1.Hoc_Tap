# Khai báo sử dụng thư viện Numpy
from unittest import result
from numpy import *
import numpy as np

#=================================================================================
# tạo ra 2 ma trận rỗng
index_cot  = []  # Mảng lưu các cột của phần tử giải (theo thứ tự)
index_hang = []  # Mảng lưu các hàng của phần tử giải (theo thứ tự)
#---------------------------------------------------------------------------------
# Tìm phần tử giải
# ưu tiên |a| = 1
# nếu ko thấy thì lấy phần tử có |a| MAX và != 0
def TimPhanTuGiai():
    global index_hang, index_cot
    index_temp = []
    maxvalue = 0
    for row in range(0, m):
        if row in index_hang:  # Bỏ qua vì hàng này đã có phần tử giải
            continue

        
        # Nếu có 1 hoặc -1 trong hàng row => chọn làm phần tử giải
        # Lưu giá trị phần tử giải, tìm vị trí trên ma trận
        if (1 in A[row, 0:n-1]) or (-1 in A[row, 0:n-1]):  
            maxvalue = 1
            hang = row
            index_temp = np.where(abs(A[row, 0:n-1]) == maxvalue)
            index_temp = index_temp[:1]
            index_temp = index_temp[0][0]
            break
        
        else:
            # Tìm phần tử có trị tuyệt đối lớn nhất trong hàng row
            max_row = np.amax(abs( A[row, 0:n-1] )) 
            if max_row > maxvalue:  
                maxvalue = max_row
                hang = row
                index_temp = np.where(abs(A[row, 0:n-1]) == maxvalue)
                index_temp = index_temp[:1]
                index_temp = index_temp[0][0]        
            
    # Lưu vị trí hàng và cột của phần tử giải              
    if maxvalue != 0:  # Lưu vị trí hàng và cột của phần tử giải
        index_hang.append(hang)
        index_cot.append(int(index_temp))
        
        print(f'\nVị trí phần tử giải: {hang+1}{index_temp+1}')
    
#==========================================================================================
# Thuật toán GaussJordan
# Quy trình khử [A|b]
def GaussJordan():
    global A
    
    TimPhanTuGiai()
    zeros_A = np.zeros([m,n])  # Tạo 1 ma trận không
    
    # Khử trên ma trận [A|b]
    for row in range(0, m):
        
        # index_hang[-1] nghĩa là chỉ hàng của 'phần tử giải' mới tìm thấy
        if row == index_hang[-1]:
            continue
        
        # tìm hệ số Z
        Z = - A[row][index_cot[-1]] / A[index_hang[-1]][index_cot[-1]]
        zeros_A[row] = A[index_hang[-1]] * Z
        
    A = A + zeros_A
    print('\n', A)
#========================================================================================
# Chuẩn hóa hệ số bằng 1
# ở mỗi hàng của [A|b] chia cho phần tử giải của hàng đó
def chuanhoaheso():
    for i in range(len(index_hang)):
        A[index_hang[i]] = A[index_hang[i]] / A[index_hang[i]][index_cot[i]]
        
#========================================================================================
rankA = 0  # Hạng của ma trận hệ số A
rankAb = 0  # Hạng của ma trận mở rộng
#----------------------------------------------------------------------------------------   
# Tìm Rank(A) và Rank(A|b)
def rank():
    global rankA, rankAb
    
    # sau khi chuẩn về hệ số 1, nếu hàng nào còn số khác 0 thì rank + 1
    for row in range(0, m):
        if np.amax(abs( A[row, 0:n-1] )) > 0:
            rankA += 1
        if np.amax(abs( A[row, 0:n]   )) > 0:
            rankAb += 1        
                    
#========================================================================================
# Tìm nghiệm X
# Dễ thấy mấy phần tử giải ko phụ thuộc nhau
# Nên cột nào không có phần tử giải thì ta đưa sang bên phải và đổi dấu

def findX(): 
    global result
    
    # Đưa các cột ko chứa phần tử giải sang bên phải và đổi dấu 
    for column in range(n-1):
        if column not in index_cot:
            for row in range(m):
                Result[row, n + column] = - Result[row, column]
                Result[row, column] = 0
    
    # trong Terminal, ma trận Result bị tràn xuống dòng nên in ra file Output     
    np.savetxt('output.txt', Result, fmt='%.5f')
                       


#========================================================================================
# Sắp xếp lại các hàng sao cho
# Ma trận  [A|E]  khi biến đổi sang [E| A^(-1)]
# nếu ở trên là 1 và ở dưới là 0 => Return 1   => giữ nguyên
# nếu ở trên là 0 và ở dưới là 1 => Return - 1 => đổi chỗ 2 hàng
def SapXepHang():
    
    # Kiểm tra 2 dãy bất kỳ 
    # So sánh 2 phần tử của 2 dãy trên cùng 1 cột
    def SoSanh(a, b, n):
        check = 0
        for i in range(n):
            if (a[i] == 1) and (b[i] < 1): return 1
            elif (a[i] < 1) and (b[i] == 1): return -1
        return  check

    for i in range(n):
        for j in range(0, m-i-1):
            if SoSanh(A[j], A[j+1], n) == -1:
                for k in range(n):
                    A[j,k], A[j+1, k] = A[j+1, k], A[j, k]
                    
                #print('Sắp xếp\n', A)


#======================================================================================
# Kiểm tra tính đúng
def Test():
    X = A[0:m, n-1:n]

    print('\nKiểm tra tính đúng =================================================')
    test = matrixA.dot(X) - b
    print(' AX - b = ')
    print(test)    
    
    
#======================================================================================
# Từ ma trận Result, ta có thể kết luận nghiệm
# Nhưng đọc ma trận dễ bị đau mắt nếu cô cho Matrix 20x20, nên phải trình bày lại và dùng Ctrl
# In ra màn hình nghiệm Hpt
def InRaManHinh():
    global rankA, rankAb, result
    
    rank()
    
    # TH1:
    # hpt vô nghiệm <=> r(A) < r(A|b)  
    if rankA < rankAb:
        print('Hpt vô nghiệm !!!')
    
    # TH2:
    # hpt có vô số nghiệm <=> r(A)=r(A|b) < số ẩn = n-1
    elif rankA < (n - 1):
        print('Hpt có vô số nghiệm !!!')
        print(' 1. cột đầu là hệ số tự do')
        print(' 2. các cột sau biểu diễn theo các nghiệm x1, x2,...Xn\n')
        findX()
         
        for i in range(len(index_cot)):
            print('x',index_cot[i]+1,' = ',Result[index_hang[i], n-1: 2*n -1])
            
        print('các nghiệm là tham số:')
        for column in range(n-1):
            if column not in index_cot:
                print ('x',column + 1,' = ','x',column + 1)
    
    # TH3:    
    # hpt có nghiệm duy nhất <=> r(A)=r(A|b) = số ẩn = n-1
    else:
        print('Hpt có nghiệm duy nhất !!!')
        findX()
        SapXepHang()
        print('\nMa trận bổ sung:\n',A,'\n')
        for i in range(len(index_cot)):
            print(f'x{i+1} = {(A[i, n-1]):f}')

        Test()    
            
#======================================================================================
# Chương trình chính
# input Ma trận bổ sung [A|b] cỡ (nxn)
A = np.loadtxt("input.txt", dtype="float")
print('Ma trận bổ sung [A|b]:\n', A)

# hệ có m pt và (n-1) ẩn
(m,n) = A.shape

# MatrixA là ma trận hệ số
# b là ma trận hệ số tự do 
matrixA = A[0:m, 0:n-1]
b = A[0:m, n-1:n]

for i in range(m):
    GaussJordan()  

print('\n==================================================================')
print ('Ma trận [A|b] sau khi khử:\n',A)    

chuanhoaheso()
print('\n=================================================================')
print ('Ma trận [A|b] sau khi chuẩn hóa hệ số 1:\n',A)    

# Tạo ma trận Result lưu nghiệm của hệ pt
Result = np.c_[A, zeros([m, n-1])]

print('\n==================================================================')
InRaManHinh()
print()
