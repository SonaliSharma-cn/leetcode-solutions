from collections import Counter

class Solution:
    def equalPairs(self, grid):
        n = len(grid)
        row_tuples = [tuple(row) for row in grid]
        row_counter = Counter(row_tuples)

        count = 0
        for col in zip(*grid):
            col_tuple = tuple(col)
            count += row_counter[col_tuple]

        return count


if __name__ == "__main__":
    n = int(input("Enter size of grid (n): "))     #3
    grid = []

    print("Enter the grid row by row:")           #3 2 1
                                                   #1 7 6
                                                   #2 7 7
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    sol = Solution()
    result = sol.equalPairs(grid)
    print("Equal row-column pairs:", result)    #1
