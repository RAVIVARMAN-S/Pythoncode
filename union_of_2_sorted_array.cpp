#include <bits/stdc++.h>
using namespace std;

class solution{
public:
    vector<int> unionOfTwoSortedArrays(vector<int> a, vector<int> b){
        vector<int> ans;
        int i=0, j=0;
        while(i<a.size() && j<b.size()){
            if(a[i]<=b[j]){
                if(ans.empty() || a[i]!=ans.back()){
                    ans.push_back(a[i]);
                }
                i++;
                }
            else{
                if(ans.empty() || b[j]!=ans.back()){
                    ans.push_back(b[j]);
                }
                j++;
                }
        }
        while(i<a.size()){
            if(ans.empty() || a[i]!=ans.back()){
                ans.push_back(a[i]);
            }
            i++;
        }
        
        while(j<b.size()){
            if(ans.empty() || b[j]!=ans.back()){
                ans.push_back(b[j]);
            }
            j++;
        }
        return ans;
        
        
    }
};
