# Thân Thị Mỹ Huyền - 20206288
# Làm việc với mảng
# Tìm kiếm 1 giá trị trong mảng đã được sắp xếp (tìm kiếm nhị phân)


# tạo mảng 
arr = [5, 6, 8, 11, 14, 18, 19, 20, 28, 99]
print('mảng đã sắp xếp: ', arr)
# nhập số cần tìm       
x = float(input('Số cần tìm = '))

#--------------------------------------------------------------------
#Trả về chỉ số của x trong arr nếu tồn tại, nếu không có sẽ trả về -1

def binary_search(arr, low, high, x):
    #Trường hợp cơ sở
    if high >= low:
        mid = (high + low) // 2
        
        # Nếu phần tử có tồn tại ở phần giữa của mảng
        if arr[mid] == x:
            return mid
        # Nếu phần tử nhỏ hơn mid, nó sẽ nằm ở phía bên trái của mảng điểm gốc là tử phần tử mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Nếu không, phần tử sẽ nằm bên phải
        else:
            return binary_search(arr, mid + 1, high, x)
        
    else:
        # Phần tử không tồn tại trong tập hợp
        return -1
    
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print('Phần tử cần tìm có chỉ số là ', str(result))
else:
    print('Phần tử cần tìm không có trong mảng')
    
    
