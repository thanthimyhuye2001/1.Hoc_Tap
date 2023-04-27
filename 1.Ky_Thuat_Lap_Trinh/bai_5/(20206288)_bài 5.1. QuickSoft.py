# Thân Thị Mỹ Huyền - 20206288
# Cài đặt giải thuật Sắp Xếp QuickSort

#-----------------------------------------------------------
# Hàm để phân vùng
def phan_vung(arr, low, high):

    # Chọn phần tử ngoài cùng bên phải làm trụ "pivot"
    pivot = arr[high]

    # Con trỏ trỏ tới phần tử lớn hơn
    i = low - 1

    # So sánh tất cả phẩn tử trong dãy với pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            # Nếu phần tử nhỏ hơn pivot được tìm thấy
            # hoán đổi nó với phần tử lớn hơn được trỏ bởi i
            i = i + 1

            # Hoán đổi phần tử ở i với phần tử ở j
            (arr[i], arr[j]) = (arr[j], arr[i])

    # Hoán đổi phần tử trụ với phần tử lớn hơn được chỉ định
    (arr[i + 1], arr[high]) = (arr[high], arr[i+1])

    # Trả về vị trí sau khi phân vùng
    return i + 1

#-----------------------------------------------------------
# Hàm thực hiện Quicksort
def quick_sort(arr, low, high):
    if low < high:

        # Tìm phần tử trụ pivot sao cho
        # phần tử nhỏ hơn trụ nằm bên trái
        # phần tử nhỏ hơn trụ nằm bên phải
        pi = phan_vung(arr, low, high)

        # Thực hiện đệ quy bên trái trụ
        quick_sort(arr, low, pi - 1)

        # Thực hiện đệ quy bên phải trụ
        quick_sort(arr, pi + 1, high)

#-----------------------------------------------------------
# Input dãy và Output dãy đã xếp
arr = [ 10, 7, 8, 9, 1, 5]
print(f'Dãy cần xếp: {arr}')
quick_sort(arr, 0, len(arr) - 1)
print(f'Dãy sau sắp xếp: {arr}')
