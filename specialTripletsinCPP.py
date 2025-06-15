class Solution {
public:
    int specialTriplets(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        unordered_map<int, int> prefix, suffix;

        // Fill suffix map with frequency count
        for (int num : nums) {
            suffix[num]++;
        }

        long long total = 0;

        for (int j = 0; j < nums.size(); j++) {
            suffix[nums[j]]--; // current j is fixed, so reduce its count

            int target = nums[j] * 2;

            long long count_i = prefix[target];
            long long count_k = suffix[target];

            total = (total + (count_i * count_k) % MOD) % MOD;

            prefix[nums[j]]++; // move j into prefix for next iteration
        }

        return total;
    }
};
