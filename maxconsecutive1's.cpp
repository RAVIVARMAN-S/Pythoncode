// Maximun consecutive of ones


#include<bits/stdc++.h>
using namespace std;

int MaxConsecutiveOnes(int arr[],int n){
    int cur = 0;
    int max = 0;
    for(int i=0;i<n;i++){
        if(arr[i]==1){
            cur++;
            if(cur>max) max=cur;
		}
        else cur=0;
	}
    return max;
}



int main(){
	int n;
    cin>> n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
	}
    cout<<MaxConsecutiveOnes(arr,n);
    return 0;
}
