# Thân Thị Mỹ Huyền - 20206288

# Đề tài: Xây dựng chương trình quản lý hồ sơ sinh viên

# File dữ liệu đầu vào: "Sinh viên.csv"

# File dữ liệu đầu ra của các chức năng hiển thị danh sách, tìm kiếm: "Kết quả.txt"
# File dữ liệu đầu ra của các chức năng cập nhập, xóa, sửa, xếp     : "Sinh viên.csv"

"""
Cột = ['MSSV', 'Họ & Tên', 'Ngày sinh', 'Khoa Viện', 'Lớp']
1. Nhập thông tin sinh viên mới
2. Thông tin danh sách sinh viên
3. Tìm kiếm thông tin sinh viên theo mã sinh viên
4. Tìm kiếm thông tin sinh viên theo tên sinh viên
5. Tìm kiếm thông tin sinh viên theo lớp sinh viên
6. Sửa thông tin sinh viên
7. Xóa thông tin sinh viên
8. Sắp xếp thông tin sinh viên theo lớp
0. Thoát ra!
"""

import csv
import operator
from numpy import *

from unittest import result
# Khai báo biến toàn cục
du_lieu_sinh_vien = 'Sinh viên.csv'
result = 'Kết quả.txt'

def Menu_chuc_nang():
    print("+----------------------------------------------------+")
    print("| HỆ THỐNG QUẢN LÝ SINH VIÊN                         |")
    print("+----------------------------------------------------+")
    print("| 1. Nhập thông tin sinh viên mới                    |")
    print("| 2. Hiển thị danh sách sinh viên                    |")
    print("| 3. Tìm kiếm thông tin sinh viên theo mã sinh viên  |")
    print("| 4. Tìm kiếm thông tin sinh viên theo tên sinh viên |")
    print("| 5. Tìm kiếm thông tin sinh viên theo lớp sinh viên |")
    print("| 6. Sửa thông tin sinh viên theo MSSV               |")
    print("| 7. Xóa thông tin sinh viên theo MSSV               |")
    print("| 8. Sắp xếp sinh viên theo lớp                      |")
    print("| 0. Thoát ra!                                       |")
    print("+----------------------------------------------------+")


#---------------------------------------------------------------------------------------------------------------------------------
# Hàm nhập thông tin sinh viên mới
def Them_sv_moi():
    global du_lieu_sinh_vien
    
    print("*---------------------------------*")
    print("1. Nhập thông tin sinh viên mới   *")
    print("*---------------------------------*")

    sv_data = []
    MSSV = input('MSSV: ')
    
    # Kiểm tra người dùng đã nhập đúng MSSV là số nguyên dương hay chưa
    typeMSSV = MSSV
    try:
        typeMSSV
        typeMSSV = int(MSSV)
        if (int(MSSV) <= 0):
            print('Vui lòng nhập lại MSSV là số nguyên dương có 8 chữ số!\n')
            Them_sv_moi()
        elif len(MSSV) != 8:
            print('Vui lòng nhập lại MSSV là số nguyên dương có 8 chữ số!\n')
            Them_sv_moi()
        else:
            # Kiểm tra sinh viên đã có trong danh sách hay chưa 
            # Nếu chưa có trong danh sách thì thêm thông tin sinh viên mới
            ton_tai = False
            with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) > 0:
                        if MSSV == row[0]:
                            ton_tai = True

            if ton_tai == True:
                print(f"\nSinh viên có mã {MSSV} đã có trong danh sách!")
            else:
                HoTen = input("Họ và tên: ")
                HoTen = HoTen.title()
                NgaySinh = (input("Ngày sinh (dd/mm/yyyy): "))
                KhoaVien = (input("Khoa viện: "))
                KhoaVien = KhoaVien.title()
                Lop = (input("Lớp: "))
                Lop = Lop.upper()
                
                cot = [MSSV, HoTen, NgaySinh, KhoaVien, Lop]
                for i in cot:
                    sv_data.append(i)
                
                with open(du_lieu_sinh_vien, "a", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows([sv_data])
                
                Xep_MSSV()
                
                print("\nThêm sinh viên mới thành công!")
                
        input("\nNhấn Enter để tiếp tục\n")        
    except:
        print('Vui lòng nhập lại MSSV là số nguyên dương có 8 chữ số!\n')
        Them_sv_moi()
        
        
#---------------------------------------------------------------------------------------------------------------------------------
# Hàm hiển thị danh sách sinh viên
def In_danh_sach():
    global du_lieu_sinh_vien

    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        ke_ngang = "+{:-<10}+{:-<30}+{:-<15}+{:-<30}+{:-<10}+\n".format('', '', '', '', '')
        list_sv = "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format('MSSV', 'Họ & tên', 'Ngày sinh', 'Khoa viện', 'Lớp')
        list_sv = ke_ngang + list_sv + ke_ngang
        
        so_luong_sv = 0
        for row in reader:
            if len(row) > 0:   
                so_luong_sv += 1           
                list_sv += "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format(row[0], row[1], row[2], row[3], row[4])
        
        if so_luong_sv == 0:
            list_sv = "Danh sách sinh viên trống!\n\n" + list_sv
            list_sv += "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format('Null', 'Null', 'Null', 'Null', 'Null')
            
        list_sv += ke_ngang            
        print()
        print(list_sv)
        
        with open(result, "w", encoding="utf-8") as f:
            f.write(list_sv)
            
    input("Nhấn Enter để tiếp tục\n")


#---------------------------------------------------------------------------------------------------------------------------------
# Hàm tìm kiếm sinh viên theo Mã Sinh Viên
# Trả về một sinh viên
def Tim_MSSV():
    global du_lieu_sinh_vien
    
    print("*-----------------------------------------*")
    print("3. Tìm kiếm thông tin theo mã sinh viên   *")
    print("*-----------------------------------------*")
    
    ke_ngang = "+{:-<10}+{:-<30}+{:-<15}+{:-<30}+{:-<10}+\n".format('', '', '', '', '')
    list_sv = "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format('MSSV', 'Họ & tên', 'Ngày sinh', 'Khoa viện', 'Lớp')
    list_sv = ke_ngang + list_sv + ke_ngang
    
    MSSV = input("Mã sinh viên: ")
    
    i = 0
    
    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if MSSV == row[0]:
                    list_sv = f'\nTìm thấy sinh viên có mã {MSSV}' + '\n\n' + list_sv
                    list_sv += "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format(row[0], row[1], row[2], row[3], row[4]) 
                    list_sv += ke_ngang
                    i += 1
                    break
    if i == 0:
        list_sv = f"\nKhông tìm thấy sinh viên mã {MSSV} !\n"
           
    print(list_sv)
    
    with open(result, "w", encoding="utf-8") as f:
        f.write(list_sv) 
     
    input("\nNhấn Enter để tiếp tục\n")
                          
                            
#---------------------------------------------------------------------------------------------------------------------------------
# Hàm tìm kiếm sinh viên theo Họ Tên
# Trả về một danh sách sinh viên    
def Tim_ten():
    global du_lieu_sinh_vien
    
    print("*---------------------------------------------*")
    print("4. Tìm kiếm thông tin theo họ tên sinh viên   *")
    print("*---------------------------------------------*")
    
    ke_ngang = "+{:-<10}+{:-<30}+{:-<15}+{:-<30}+{:-<10}+\n".format('', '', '', '', '')
    list_sv = "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format('MSSV', 'Họ & tên', 'Ngày sinh', 'Khoa viện', 'Lớp')
    list_sv = ke_ngang + list_sv + ke_ngang
    
    i = 0
    
    HoTen = input("Nhập họ và tên sinh viên: ")
    HoTen = HoTen.title()
    
    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            
            if len(row) > 0:
                if HoTen == row[1]:
                    list_sv += "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format(row[0], row[1], row[2], row[3], row[4])
                    i  += 1
    if i == 0:
        list_sv = f"\nKhông tìm thấy sinh viên tên {HoTen} !"
    else:
        list_sv = f'\nTìm thấy {i} sinh viên có tên {HoTen}' + '\n\n' + list_sv + ke_ngang
    
    print(list_sv)
    
    with open(result, "w", encoding="utf-8") as f:
        f.write(list_sv) 
    
    input("\nNhấn Enter để tiếp tục\n")
        
        
#---------------------------------------------------------------------------------------------------------------------------------
# Hàm tìm kiếm sinh viên theo Lớp
# Trả về một danh sách sinh viên
def Tim_lop():
    global du_lieu_sinh_vien
    
    print("*------------------------------------------*")
    print("5. Tìm kiếm thông tin theo lớp sinh viên   *")
    print("*------------------------------------------*")
    
    ke_ngang = "+{:-<10}+{:-<30}+{:-<15}+{:-<30}+{:-<10}+\n".format('', '', '', '', '')
    list_sv = "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format('MSSV', 'Họ & tên', 'Ngày sinh', 'Khoa viện', 'Lớp')
    list_sv = ke_ngang + list_sv + ke_ngang
    
    i = 0
    
    Lop = input("Sinh viên thuộc lớp: ")
    Lop = Lop.upper()
    
    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if Lop == row[4]:
                    list_sv += "|{:<10}|{:<30}|{:<15}|{:<30}|{:<10}|\n".format(row[0], row[1], row[2], row[3], row[4])
                    i  += 1
    
    if i == 0:
        list_sv = f"\nKhông tìm thấy sinh viên học lớp {Lop} !"
    else:
        list_sv = f'\nTìm thấy {i} sinh viên học lớp {Lop}' + '\n\n' + list_sv + ke_ngang
    
    print(list_sv)
    
    with open('kết quả.txt', "w", encoding="utf-8") as f:   
        f.write(list_sv) 
                        
    input("\nNhấn Enter để tiếp tục\n")
    
   
#---------------------------------------------------------------------------------------------------------------------------------
# Hàm cập nhật thông tin sinh viên                        
def sua():
    global du_lieu_sinh_vien

    print("*-------------------------------------------*")
    print("6. Sửa thông tin sinh viên theo MSSV        *")
    print("*-------------------------------------------*")

    sua_sv = []
    MSSV = input("\nNhập MSSV của sinh viên bạn muốn cập nhật thông tin: ")

    # Kiểm tra sinh viên đã có trong danh sách hay chưa 
    # Nếu có trong danh sách thì cập nhật thông tin sinh viên đó
    ton_tai = False
    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        for row in reader:
            if len(row) > 0:
                if MSSV == row[0]:
                    
                    ton_tai = True
                    sv_data = []
                    
                    HoTen = input("Họ và tên: ")
                    HoTen = HoTen.title()
                    NgaySinh = (input("Ngày sinh (dd/mm/yyyy): "))
                    KhoaVien = (input("Khoa viện: "))
                    KhoaVien = KhoaVien.title()
                    Lop = (input("Lớp: "))
                    Lop = Lop.upper()
                    
                    sv_data.append(MSSV)
                    sv_data.append(HoTen)
                    sv_data.append(NgaySinh) 
                    sv_data.append(KhoaVien) 
                    sv_data.append(Lop)
                        
                    sua_sv.append(sv_data)
                else:
                    sua_sv.append(row)

    if ton_tai == True:
        print(f' Sinh viên có mã {MSSV} đã cập nhật thông tin! ')
        
        with open(du_lieu_sinh_vien, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(sua_sv)
            
    else:
        print(f"\nSinh viên có mã {MSSV} không có trong danh sách")

    input("\nNhấn Enter để tiếp tục\n")


#---------------------------------------------------------------------------------------------------------------------------------
# Hàm xóa sinh viên theo MSSV
def Xoa():
    global du_lieu_sinh_vien
  
    print("*--------------------------------------*")
    print("7. Xóa thông tin sinh viên theo MSSV   *")
    print("*--------------------------------------*")
    
    xoa_sv = []
    
    MSSV = input("Nhập mã sinh viên bạn muốn xóa: ")
    
    ton_tai = False
    
    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        for row in reader:
            if len(row) > 0:
                if MSSV != row[0]:
                    xoa_sv.append(row)
                else:
                    ton_tai = True

    if ton_tai == True:
        with open(du_lieu_sinh_vien, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(xoa_sv)
            
        print(f"\nSinh viên có mã {MSSV} đã bị xóa!")
    else:
        print(f"\nSinh viên có mã {MSSV} không có trong danh sách!")

    input("\nNhấn Enter để tiếp tục\n")


#---------------------------------------------------------------------------------------------------------------------------------
# Hàm sắp xếp sinh viên theo lớp
def Xep_lop():
    print("*-------------------------------*")
    print("8. Sắp xếp sinh viên theo lớp   *")
    print("*-------------------------------*")
    
    global du_lieu_sinh_vien
    
    danh_sach_sv = []
    
    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        for row in reader:
            if len(row) != 0:
                danh_sach_sv.append(row)
              
    xep_sv = sorted(danh_sach_sv,key = operator.itemgetter(-1) )   
    
    with open(du_lieu_sinh_vien, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(xep_sv)
        
    In_danh_sach()

    
#---------------------------------------------------------------------------------------------------------------------------------
# Hàm sắp xếp sinh viên theo MSSV
def Xep_MSSV():
    
    global du_lieu_sinh_vien
    
    danh_sach_sv = []
    
    with open(du_lieu_sinh_vien, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
        for row in reader:
            if len(row) != 0:
                danh_sach_sv.append(row)
              
    xep_sv = sorted(danh_sach_sv,key = operator.itemgetter(0) )   
    
    with open(du_lieu_sinh_vien, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(xep_sv)
        
#---------------------------------------------------------------------------------------------------------------------------------
# Các chức năng của chương trình
while True:
    Menu_chuc_nang()
    Xep_MSSV()

    choice = input("\nChọn 1 trong các chức năng ở trên (0-8) : ")
    print()
    if choice == '1':
        Them_sv_moi()
    elif choice == '2':
        print("*------------------------*")
        print("2. Danh sách sinh viên   *")
        print("*------------------------*")
        In_danh_sach()
    elif choice == '3':
        Tim_MSSV()
    elif choice == '4':
        Tim_ten()  
    elif choice == '5':
        Tim_lop()          
    elif choice == '6':
        sua()
    elif choice == '7':
        Xoa()
    elif choice == '8':
        Xep_lop()
    elif choice == '0':
        print("\nBạn đã chọn thoát chương trình!")
        break
    else:
        print("\nHệ thống chưa có chức năng này!")
        print("\nVui lòng chọn 1 trong các chức năng trên!")
        input("\nNhấn Enter để tiếp tục\n")        
        
