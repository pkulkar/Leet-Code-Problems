#include <math.h>
#include<limits.h> 
#include<stdlib.h> 
int reverse(int x) {
   long number=0;
    int i=0;
    int j=0;
    int arr[100];
    int remainder;
  
    for(;;){
    
    remainder = x % 10;
    x=x/10;
        i++;
    arr[j]=remainder;
        printf("arr[%d]=%d",j,arr[j]);
        j++;
        if(x==0){
            break;
        }
    }
    j=0;
    int k;
 
    for(k=i-1;k>-1;k--){
        number=(pow(10,k)*arr[j])+number;
        j++;
    }
      if(number>2147483647 || number < -2147483647){
        return 0;
    }
    return number;
}