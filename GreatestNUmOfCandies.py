from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result

candies = list(map(int, input("Candies list (space se alag): ").split()))
extraCandies = int(input("Extra candies kitni hain? "))

sol = Solution()
output = sol.kidsWithCandies(candies, extraCandies)
print(output)
