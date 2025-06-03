from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed) 

        for i in range(length):  
            if flowerbed[i] == 0:  
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n == 0
flowerbed_input = input("Enter flowerbed as 0s and 1s : ")            #1 0 0 0 1
flowerbed = list(map(int, flowerbed_input.strip().split()))             #1
n = int(input("Enter number of flowers to plant: "))

sol = Solution()
result = sol.canPlaceFlowers(flowerbed, n)

print("Can place flowers?" , result)                         #True
