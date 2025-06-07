from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:   
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        return max_sum / k

nums_input = input("Enter the list of numbers separated by spaces: ")  # Example: 1 12 -5 -6 50 3
nums = list(map(int, nums_input.strip().split()))

k = int(input("Enter the value of k: "))                      #4
sol = Solution()
result = sol.findMaxAverage(nums, k)

print(f"Maximum average of subarray of length {k} is: {result:.5f}")         #12.75000
