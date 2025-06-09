class Solution3:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left)

        return max_len


# ✅ Input + Output for Question 3
print("\n--- Q3: Longest Subarray After Deleting One ---")
nums3 = list(map(int, input("Enter binary list (space-separated): ").split()))
sol3 = Solution3()
print("Output:", sol3.longestSubarray(nums3))
