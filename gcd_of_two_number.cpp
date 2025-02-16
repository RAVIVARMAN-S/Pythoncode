#include<bits/stdc++.h>
using namespace std;
int main(){
   int num1,num2;
   cout<<"enter the valur:";
   cin>>num1>>num2;
   while(num1!=0 && num2!=0) // checks value of num1 and num2 are 0 until the condition false
   {
    if(num1>=num2){num1=num1%num2;}
    else{num2=num2%num1;}

   }
   if(num1==0){cout<<num2;}//if num1 is '0' means print value of num2
   else{cout<<num1;} //if num2 is '0' means print value of num1
   
   
}
