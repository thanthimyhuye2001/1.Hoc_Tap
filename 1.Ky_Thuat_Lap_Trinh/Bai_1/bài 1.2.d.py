'''
Thân Thị Mỹ Huyền - 20206288
In được cây thông nô en theo chiều cao nhập vào '''

n = int(input("cây cao bao nhiêu: "))
for i in range(1,2*n,2):
    print(('*'*i).center(2*n))
    
for goc_cay in range(2):
    print(('| |').center(2*n))
    
print(('\===/').center(2*n))
