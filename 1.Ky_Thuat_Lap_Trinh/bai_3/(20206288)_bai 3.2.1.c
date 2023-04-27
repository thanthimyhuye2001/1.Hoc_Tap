//Than Thi My Huyen - 20206288

#include<stdio.h>

int main() 
{
    int a = 3;
    int b = 4;
    
    printf("Nhap a = ");
    scanf("%d", &a);
    
    printf("Nhap b = ");
    scanf("%d", &b);
       
    int *p1, *p2;
    // tro p1 den dia chi o nho cua a
    p1 = &a;
    // tro p2 den dia chi o nho cua b
    p2 = &b;

    // cong hai so su dung con tro
    int sum;
    sum = *p1 + *p2;

    printf("Tong hai so = %d", sum);
    return (0);
}
