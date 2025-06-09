class Solution2:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


# ✅ Input + Output for Question 2
print("\n--- Q2: Max Consecutive Ones III ---")
nums2 = list(map(int, input("Enter binary list (space-separated): ").split()))
k2 = int(input("Enter k (max flips): "))
sol2 = Solution2()
print("Output:", sol2.longestOnes(nums2, k2))

