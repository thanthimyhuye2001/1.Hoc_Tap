// Than Thi My Huyen - 20206288
// vi python ko ho tro con tro nen em xin phep dung C

#include<stdio.h>
#include<conio.h>

int string_ln(char*);

int main() {
   char str[20];
   int length;
   
   printf("\nNhap chuoi bat ky: ");
   gets(str);
   
   length = string_ln(str);
   printf("\nDo dai chuoi %s la: %d", str, length);
  return(0);
}

// Hàm dem do dai chuoi su dung con tro
int string_ln(char*p)
{
   int count = 0;
   while (*p != '\0') {
      count++;
      p++;
   }
   return count;
}
