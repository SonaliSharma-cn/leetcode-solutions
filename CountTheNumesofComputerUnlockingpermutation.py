from math import comb
from collections import defaultdict
from typing import List
import sys

MOD = 10**9 + 7

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)

        # Factorial and inverse factorial precomputation
        max_n = n
        fact = [1]*(max_n+1)
        inv_fact = [1]*(max_n+1)
        for i in range(2, max_n+1):
            fact[i] = fact[i-1]*i % MOD

        inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
        for i in reversed(range(1, max_n)):
            inv_fact[i] = inv_fact[i+1]*(i+1)%MOD

        def multinomial(sizes):
            total = sum(sizes)
            res = fact[total]
            for x in sizes:
                res = (res * inv_fact[x]) % MOD
            return res

        # Step 1: Construct parent mapping
        min_parent = [-1]*n
        for i in range(1, n):
            min_p = -1
            for j in range(i):
                if complexity[j] < complexity[i]:
                    min_p = j
                    break
            if min_p == -1:
                return 0
            min_parent[i] = min_p

        # Step 2: Build tree
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            p = min_parent[i]
            tree[p].append(i)

        # Step 3: DFS to compute permutations
        sys.setrecursionlimit(10**7)

        def dfs(u):
            total_size = 0
            res = 1
            sizes = []
            for v in tree[u]:
                dp_v, size_v = dfs(v)
                res = (res * dp_v) % MOD
                sizes.append(size_v)
                total_size += size_v
            res = (res * multinomial(sizes)) % MOD
            return res, total_size + 1

        ans, _ = dfs(0)
        return ans % MOD

if __name__ == "__main__":
    complexity = list(map(int, input("Enter complexity values (space-separated): ").split()))
    sol = Solution()
    result = sol.countPermutations(complexity)
    print("Total valid permutations:", result)
