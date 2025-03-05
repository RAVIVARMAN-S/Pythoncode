// intersection of two sorted array


#include<bits/stdc++.h>
using namespace std;


vector<int> interSection2Sortedarrays(vector<int>a, vector<int>b) {
    vector<int> ans;
    int m = a.size();
    int n = b.size();
    int i = 0;
    int j = 0;
    while(i < m && j < n){
        if(a[i] == b[j]){
            ans.push_back(a[i])
            i++;
            j++;
        }
        else if(a[i] < b[j]) i++;
        else j++;
    }
    return ans;
}
        

int main(){
    int m,n;
	cin >> m>> n;
	vector<int> a;
	vector<int> b;
	for(int i=0;i<m;i++){
		int temp;
		cin >> temp;
		a.push_back(temp);
	}

	for(int i=0;i<n;i++){
		int temp;
		cin >> temp;
		b.push_back(temp);
	}

	vector<int> ans = interSection2Sortedarrays(a, b);
	for(auto k: ans){
		cout<< k <<" ";
		return 0;
	}
  
}
