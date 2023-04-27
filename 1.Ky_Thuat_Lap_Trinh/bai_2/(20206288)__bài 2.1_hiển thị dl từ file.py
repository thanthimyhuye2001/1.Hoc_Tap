'''
Thân Thị Mỹ Huyền - 20206288
file<->màn hình:
Viết chương trình hiển thị dữ liệu từ file/thêm dữ liệu vào file, xóa dữ liệu từ file, cập nhật dữ liệu từ file.
'''
# Mở để đọc file
f = open("C:/Users/HAN NGA/Downloads/Học Python/Kỹ Thuật lập trình/bài 2/test.txt",'r')
a = f.read()
# Đóng file
f.close()

# hiển thị dữ liệu từ file
print(a)