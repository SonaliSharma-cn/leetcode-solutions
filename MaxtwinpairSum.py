
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

class Solution:
    def pairSum(self, head):
     
        nums = [] 

        current = head  

        while current: 
            nums.append(current.val) 
            current = current.next  
        
        max_sum = 0  

        n = len(nums)  

        for i in range(n // 2): 
            twin_sum = nums[i] + nums[n - 1 - i] 
            max_sum = max(max_sum, twin_sum) 

        return max_sum  

        