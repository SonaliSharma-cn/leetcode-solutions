class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
       total_ways = 0
       for a in range(min(limit, n) + 1):
            low_b = max(0, n - a - limit)
            high_b = min(limit, n - a)

            if low_b <= high_b:
                count_b = high_b - low_b + 1
                total_ways += count_b

       return total_ways 
n = int(input("Total candies : "))           #5
limit = int(input("each kid get maximum of candies: "))        #2

sol = Solution()
result = sol.distributeCandies(n, limit)

print("Candies ditribution in proper way:", result)    #3