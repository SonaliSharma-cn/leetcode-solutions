from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0                    
        right = len(height) - 1      
        max_water = 0                

        while left < right:         
            width = right - left     
            min_height = min(height[left], height[right]) 
            current_area = width * min_height             
            max_water = max(max_water, current_area)       

            if height[left] < height[right]:  
                left += 1
            else:
                right -= 1

        return max_water    
input_str = input("heights of lines: ")         #1 8 6 2 5 4 8 3 7

height_list = list(map(int, input_str.strip().split()))

solution = Solution()
result = solution.maxArea(height_list)

print("Maximum water which can come in the container:", result)    #49