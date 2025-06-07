from typing import List
from math import prod

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        for mask in range(1, (1 << n) - 1):  # all non-empty subsets excluding full set
            subset1 = []
            subset2 = []

            for i in range(n):
                if (mask >> i) & 1:
                    subset1.append(nums[i])
                else:
                    subset2.append(nums[i])
            
            if not subset1 or not subset2:
                continue  # skip if any subset is empty

            if prod(subset1) == target and prod(subset2) == target:
                return True

        return False

if __name__ == "__main__":
    nums = list(map(int, input("Enter space-separated distinct positive integers (nums): ").split()))
    target = int(input("Enter target product: "))

    sol = Solution()
    result = sol.checkEqualPartitions(nums, target)

    print("Output:", result)
