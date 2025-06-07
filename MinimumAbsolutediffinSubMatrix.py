from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        result = []

        for i in range(m - k + 1):
            row_result = []
            for j in range(n - k + 1):
                values = []

                for x in range(i, i + k):
                    for y in range(j, j + k):
                        values.append(grid[x][y])

                values = list(set(values))

                if len(values) == 1:
                    row_result.append(0)
                else:
                    values.sort()
                    min_diff = float('inf')
                    for z in range(1, len(values)):
                        min_diff = min(min_diff, abs(values[z] - values[z - 1]))  
                    row_result.append(min_diff)
            result.append(row_result)

        return result

m = int(input("Enter number of rows: "))           #2
n = int(input("Enter number of columns: "))               #2

print("Enter the grid rows (space-separated):")       #1 8 
                                                      #3 -2
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)


k = int(input("Enter value of k: "))               #2
sol = Solution()
ans = sol.minAbsDiff(grid, k)
print("Output:")                                   #[2]
for row in ans:
    print(row)
