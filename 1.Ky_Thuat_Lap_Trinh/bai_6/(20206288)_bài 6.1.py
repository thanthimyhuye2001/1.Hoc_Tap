# Thân Thị Mỹ Huyền - 20206288
# Thực hành đệ quy qua cài đặt bài toán:
# Tính số Fibonaci F(n)

# Hàm đệ quy tính số Fibonaci thứ n
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)

# Khối lệnh có thể phát sinh lỗi
try:
   # Nhập giá trị n từ bàn phím
   # Ép kiểu dữ liệu sang số nguyên
   n = int(input('n = '))
  
   # Sử dụng cấu trúc rẽ nhánh xử lý trường hợp n <= 0
   if n <= 0:
       print('Vui lòng nhập số nguyên dương!')
   else:
       print(f'Số Fibonaci thứ {n} là: F({n}) = {Fibonacci(n)}')
       
# khối lệnh được thực thi khi lỗi xảy ra
except:
   print('Định dạng đầu vào không hợp lệ!')
