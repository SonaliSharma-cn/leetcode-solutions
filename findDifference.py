from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

# User input
nums1 = list(map(int, input("Enter nums1 values separated by space: ").split()))   #1 2 3
nums2 = list(map(int, input("Enter nums2 values separated by space: ").split()))   #2 4 6
sol = Solution()
print("Difference:", sol.findDifference(nums1, nums2))            #[[1, 3], [4, 6]]
