#include<cs50.h>
#include<stdio.h>
void mario(int height);

int main(void)
{
    int n=-1;
    do
    {
     n=get_int("Enter the height : ");
    }
    while (n<0||n>23);
    mario(n);
}
void mario(int n)
{
    for(int i=0; i<n; i++)
    {
     for(int j=0;j<n-1-i;j++)
     {
            printf(" ");
     }

     for(int k=0;k<i+2;k++)
     {
      printf("#");
     }
    printf("\n");
    }
}