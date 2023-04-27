# Thân Thị Mỹ Huyền - 20206288
# Làm việc với mảng
# Tìm kiếm bảng băm (OPTION)

#-------------------------------------------------------------------
#Lớp Bảng Băm
class BangBam:
    # khởi tạo bảng băm
    def __init__(self, kich_thuoc = 10):
        self.danh_sach = [None for _ in range(kich_thuoc)]
    
    # chuyển bảng băm về kiểu chuỗi
    def __str__(self):
        kq = '['        
        STT1 = 0
        for x in self.danh_sach:      
            STT1 += 1              
            if STT1 != 1:
                kq = kq + ', '
            #end if
            
            if x is None:             
                kq = kq + '[None]' 
            else:
                kq = kq + '['
                STT2 = 0
                for e in x:
                    STT2 += 1
                    if STT2 != 1:
                        kq = kq + ', '
                    #end if
                    kq = kq + str(e[0]) + ': ' + str(e[1])
                #end for               
                kq = kq + ']'
            #end if    
        #end for
        kq = kq + ']'
        return kq
    
    #----------------------------------------------------------------
    # trả về giá trị băm của khóa key
    def bam(self, key):
        kich_thuoc = len(self.danh_sach)
        return hash(key) % kich_thuoc
    
    #----------------------------------------------------------------
    # Đưa (Thêm) cặp [key, gia_tri] vào bảng băm
    def them(self, key, gia_tri):
        chi_muc = self.bam(key)
        if self.danh_sach[chi_muc] is None:
            # Thêm mới 
            self.danh_sach[chi_muc] = list()
            self.danh_sach[chi_muc].append([key, gia_tri])
        else:
            # Cập nhật 
            cap_nhat = False
            for x in self.danh_sach[chi_muc]:
                if x[0] == key:
                    x[1] = gia_tri
                    cap_nhat = True
                    break
            
            if cap_nhat == False:
                self.danh_sach[chi_muc].append([key, gia_tri])
                
    #----------------------------------------------------------------            
    # Lấy ra 1 giá trị từ bảng băm với khóa "key" tương ứng
    def lay(self, key):
        chi_muc = self.bam(key)
        if self.danh_sach[chi_muc] is None:
            return None
        else:
            for x in self.danh_sach[chi_muc]:
                if x[0] == key:
                    return x[1]
    
            
    def __setitem__(self, key, gia_tri):
        self.them(key, gia_tri)
        
    def __getitem__(self, key):
        return self.lay(key)
    
#----------------------------------------------------------------     
# Tạo đối tượng bảng băm 
# Thêm vào bảng băm các cặp giá trị ngẫu nhiên [key, giá trị] vào bảng băm
# Xuất chuỗi mô tả bảng băm sau mỗi lần thêm
# Nhập vào 1 key, lấy và xuất ra giá trị tương ứng với khóa đó trong bảng băm

def main():
    bang_bam = BangBam(10)
    import random 
    for _ in range(18):
        key = random.randint(0,9)
        gia_tri = random.randint(0,100)
        
        print(f'Thêm khóa = {key}, Giá trị = {gia_tri}')
        bang_bam[key] = gia_tri
        print(bang_bam)
        print()
        
    key = int(input('Nhập vào một khóa: '))
    gia_tri = bang_bam[key]
    
    print(f'Khóa {key} có giá trị là {gia_tri} ')
        
        
main()
