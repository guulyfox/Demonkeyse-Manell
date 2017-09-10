#include<stdio.h>

long factorial(int n);

int main(){
   int n;
   long a;
   printf("please input a number!\n");
   scanf("xxx %d", &n);
   a = factorial(n);
   printf("The factorial of %d result is %ld", n, a);
}


long factorial(int n){
	
	long result;
   
   if(n==0 || n==1){
	
	result = 1;
}else{
	result = factorial(n-1)*n; //key
}
	return result;
}
