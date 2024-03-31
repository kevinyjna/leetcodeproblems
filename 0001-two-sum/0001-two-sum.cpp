class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> hash;
        int comp;
        for (int i = 0; i < nums.size(); i++) {
            comp = target - nums[i]; // 9-2 = 7
            if (hash.find(comp) != hash.end()) {
                return {hash[comp], i};
            }
            hash.insert({nums[i], i});
        }
        return {};
        
    }
};