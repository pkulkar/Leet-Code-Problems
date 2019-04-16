bool isPalindrome(int x) {
    if(x<0){
        return false;
    }
    int a[50];
    int i=0;
    while(x/10!=0){
       a[i]=x%10;
        x=x/10;
        i++;
    }
      int y=i;
    a[i]=x;
    /*for(i=y;i>-1;i--){
        printf("%d\n",a[i]);
    }*/
  
    int z=0;
    for(i=y;i>y/2;i--){
  
        if(z<=i){
            if(a[i]!=a[z] ){
            return false;   
            }
        }
        z++;
    }
 
    return true;
}