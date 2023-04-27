// Than Thi My Huyen - 20206288
// vi python ko ho tro con tro nen em xin phep dung C

#include <stdio.h>
#include <math.h>
int main()
{
    int size, i, arr[10];
    int *p;
    int sum = 0;
    
    // tro p den dia chi o nho cac phan tu trong mang
    p = &arr[0];
    
    printf("\nNhap kich co mang: ");
    scanf("%d", &size);
 
    printf("\nNhap %d phan tu: \n", size);
    for (i = 0; i < size; i++) 
	{
        printf("Nhap arr[%d] = ", i + 1);
        scanf("%d", &arr[i]);
    }
       
    // tinh tong cac phan tu trong mang su dung con tro
    for (i = 0; i < size; i++)
    {
        sum = sum + *p;
        p++;
    }
    printf("Tong cac phan tu trong mang = %d", sum);
    return (0);
}
