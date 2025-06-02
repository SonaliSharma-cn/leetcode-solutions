from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     num_map={}
     for i,num in enumerate(nums):
      diff=target-num

      if diff in num_map:
        return[num_map[diff],i]      
      num_map[num]=i
     return []    
nums_input = input("Numbers  (comma  separated): ")  # Example: 2,7,11,15
nums = list(map(int, nums_input.split(",")))  # '2,7,11,15' → [2, 7, 11, 15]

target = int(input("Target number : "))  # Example: 9

solution = Solution()
result = solution.twoSum(nums, target)

print("Result:", result)