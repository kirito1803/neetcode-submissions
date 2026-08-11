class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int different = target - nums[i];

            if (seen.find(different) != seen.end()) {
                return {seen[different], i};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};