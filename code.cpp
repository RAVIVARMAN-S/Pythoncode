#include <bits/stdc++.h>
using namespace std;

class solution{
public:
    int findSingleElement(int arr[], int n){
        map<int,int> m;
        for(int i=0;i<n;i++){
            m[arr[i]]++;
        }
        for(auto k:m){
            if(k.second==1){
                return k.first;
            }
        }
        
        
    }
};
