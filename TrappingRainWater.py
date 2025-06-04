from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


input_str = input("Enter the heights of bars : ")        #0 1 0 2 1 0 1 3 2 1 2 1
height_list = list(map(int, input_str.strip().split()))
solution = Solution()
result = solution.trap(height_list)
print("Trapped water amount:", result)               #6
