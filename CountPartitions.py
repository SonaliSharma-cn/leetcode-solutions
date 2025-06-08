from collections import deque
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        dp = [0] * (n + 1)
        dp[0] = 1 
        
        max_dq = deque() 
        min_dq = deque()  
        
        left = 0
        
        for right in range(n):
           
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            
         
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            
           
            while nums[max_dq[0]] - nums[min_dq[0]] > k:
             
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1
            
         
            dp[right+1] = (dp[right+1] + dp[left]) % MOD
            
           
          
        prefix_dp = [0] * (n + 2)
        prefix_dp[0] = 0
        for i in range(n + 1):
            prefix_dp[i+1] = (prefix_dp[i] + dp[i]) % MOD
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        max_dq.clear()
        min_dq.clear()
        left = 0
        
        for right in range(n):
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)
            
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)
            
            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1
            
            
            dp[right+1] = (dp[right+1] + (prefix_dp[right+1] - prefix_dp[left]) ) % MOD
            
           
            prefix_dp[right+2] = (prefix_dp[right+1] + dp[right+1]) % MOD
        
        return dp[n] % MOD

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements (space-separated): ").split()))
    k = int(input("Enter the max allowed difference (k): "))
    
    sol = Solution()
    result = sol.countPartitions(nums, k)
    print("Number of valid partitions:", result)        