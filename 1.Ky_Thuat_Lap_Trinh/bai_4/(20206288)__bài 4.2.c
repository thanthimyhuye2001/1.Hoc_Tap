// Than Thi My Huyen - 20206288
// vi python ko ho tro con tro nen em xin phep dung C

#include<stdio.h>
#include<conio.h>
 
int main() 
{
   int size, i, arr[10];
   int *ptr;
   
   // tro p den dia chi o nho cua phan tu trong mang theo chieu xuoi
   p = &arr[0];
 
   printf("\nNhap kich co mang: ");
   scanf("%d", &size);
 
   printf("\nNhap %d phan tu: \n", size);
   for (i = 0; i < size; i++) {
       printf("Nhap arr[%d] = ", i + 1);
       scanf("%d", &arr[i]);
   }
   
   // tro p den dia chi o nho cua phan tu trong mang theo chieu nguoc lai
   p = &arr[size - 1];
 
   printf("\nHien thi cac phan tu mang theo chieu dao nguoc:");
   for (i = size - 1; i >= 0; i--) 
   {
      printf("\narr[%d] = %d", size-i, *p);
      p--;
   }
 
   return(0);
}
