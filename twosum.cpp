//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0;i<nums.size()-1;i++){
            for(int j=i+1;j<nums.size();j++){
                if((nums[i]+nums[j])==target){ 
                    return {i,j}; // retuen i,j index value
                }
            }
        }
        return {};
    }
};
