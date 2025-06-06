from collections import Counter
from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter()      
        operations = 0         

        for num in nums:        
            target = k - num    
            if count[target] > 0:   
                operations += 1     
                count[target] -= 1
            else:
                count[num] += 1     

        return operations 
nums_str = input("Numbers : ")
nums = list(map(int, nums_str.split()))

k = int(input("Target sum : "))

sol = Solution()

result = sol.maxOperations(nums, k)
print("Maximum operations:", result)    