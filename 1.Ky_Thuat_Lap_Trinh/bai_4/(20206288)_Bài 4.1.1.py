# Thân Thị Mỹ Huyền - 20206288
# Làm việc với mảng
# Tìm kiếm 1 giá trị có trong mảng hay không, tìm min, max


# input mảng 
arr = [0, 9, 7, 2, 4, 9, 0, 4, 7, 4, 6, 1, 0]
print (arr)

#-------------------------------------------------
#Tìm kiếm 1 giá trị có trong mảng hay không
number = int(input('nhập số muốn kiểm tra = '))
ket_qua = number in arr

if ket_qua == True:
    print(number,'có trong mảng')
if ket_qua == False:
    print(number,'không có trong mảng')

#--------------------------------------------------
#So sánh từng phần tử trong mảng với giá trị đầu tiên để tìm ra giá trị Min, Max
length = len(arr)
max = arr[0]
min = arr[0]
for i in range(1,length):
        
        #thay đổi giá trị max nếu tìm được số lớn hơn
        if max < arr[i]:
            max = arr[i]
        #thay đổi giá trị min nếu tìm được số nhỏ hơn
        if min > arr[i]:
            min = arr[i]
            
print('min = ',min,'\nmax = ',max)    