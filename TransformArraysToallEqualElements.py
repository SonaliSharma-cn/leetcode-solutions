from typing import List

class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        def can_convert(target: int) -> bool:
            arr = nums[:]  
            ops = 0
            n = len(arr)

            for i in range(n - 1):
                if arr[i] != target:
                 
                    arr[i] = -arr[i]
                    arr[i + 1] = -arr[i + 1]
                    ops += 1
                    if ops > k:
                        return False
           
            return arr[-1] == target

        
        return can_convert(1) or can_convert(-1)
if __name__ == "__main__":
    nums = list(map(int, input("Enter the list of integers (space-separated): ").split()))
    k = int(input("Enter the maximum allowed operations (k): "))
    
    sol = Solution()
    result = sol.canMakeEqual(nums, k)
    print("Can make all elements equal using at most k operations?:", result)
    