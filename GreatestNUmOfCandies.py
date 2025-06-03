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

candies = list(map(int, input("Candies list (space se alag): ").split()))         #2 3 5 1 3
extraCandies = int(input("Extra candies kitni hain? "))                       #3

sol = Solution()
output = sol.kidsWithCandies(candies, extraCandies)
print(output)                                                             #[True, True, True, False, True]
