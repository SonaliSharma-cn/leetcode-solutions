from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        freq = list(count.values())
        return len(freq) == len(set(freq))

# User input
arr = list(map(int, input("Enter numbers separated by space: ").split()))       #1 2 2 1 1 3
sol = Solution()
print("Are occurrences unique?:", sol.uniqueOccurrences(arr))                #True
