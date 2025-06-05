from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0  

        for i in range(len(nums)):
            if nums[i] != 0:          
                nums[non_zero_index] = nums[i] 
                non_zero_index += 1   

        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

nums = list(map(int, input("Enter numbers separated by space: ").split()))       #0 1 0 3 12

Solution().moveZeroes(nums)

print("Output after moving zeroes to the end:")     #[1, 3, 12, 0, 0]
print(nums)
