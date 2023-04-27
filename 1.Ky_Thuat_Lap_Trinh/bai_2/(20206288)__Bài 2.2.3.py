'''
Thân Thị Mỹ Huyền - 20206288
In được một số loại cây theo tùy chọn người dùng nhập '''

n = str(input("vui lòng nhập tên 1 trong 3 cây sau: cây chổi, cây noel, cây cỏ\n"))
a = 'cây chổi'
b = 'cây noel'
c = 'cây cỏ'
if (n != a and n != b and n != c): 
    print('vui lòng nhập đúng tên các cây theo yêu cầu')
else:    
    if n == a:
        for than_cay_choi in range(8):
            print('   ||')
        for i in range(2,8,2):
            print(('*'*i).center(8))  
              
    elif n == b:
        for j in range(1,10,2):
            print(('*'*j).center(10))
        print(('| |').center(10))
        print(('\===/').center(10))  
          
    else:
        print("\|/ \|/ \|/")           