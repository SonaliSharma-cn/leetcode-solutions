class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0

        res = float('inf')  
        for i in range(1, n):
            part1 = i
            part2 = n - i
            if part1 <= k and part2 <= k and m <= k:
                cost = part1 * part2
                res = min(res, cost)

       
        for i in range(1, m):
            part1 = i
            part2 = m - i
            if part1 <= k and part2 <= k and n <= k:
                cost = part1 * part2
                res = min(res, cost)

        return 0 if res == float('inf') else res
if __name__ == "__main__":
    print("Enter dimensions and max allowed length without cut:")
    n = int(input("Enter length (n): "))
    m = int(input("Enter width (m): "))
    k = int(input("Enter max allowed piece length (k): "))

    sol = Solution()
    result = sol.minCuttingCost(n, m, k)
    print("Minimum Cutting Cost:", result)