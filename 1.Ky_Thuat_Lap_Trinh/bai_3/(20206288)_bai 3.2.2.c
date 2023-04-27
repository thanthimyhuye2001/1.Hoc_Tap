// Than Thi My Huyen - 20206288
// vi python ko ho tro con tro nen em xin phep dung C

#include<stdio.h>
 
// Tham so dau vao là 2 bien con tro kieu int
// dung * de lay giá tri cua bien mà con tro dang tro toi
// ham trao doi gia tri hai bien su dung con tro
void Trao_doi(int *a, int *b) 
{
   int temp;
   //lay gia tri cua bien ma con tro  a  dang tro toi va gan cho bien 'temp' 
   temp = *a;
   *a = *b;
   *b = temp;
}
  
int main() 
{
   int a, b;
   printf("Number1: ");
   scanf("%d", &a);
   printf("Number2: ");
   scanf("%d", &b);
  
   Trao_doi(&b, &a);
    
   printf("\nSau khi trao doi");
   printf("\nNumber1: %d", a);
   printf("\nNumber2: %d", b);
  
   return (0);
}
