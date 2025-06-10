from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude

# User input
gain = list(map(int, input("Enter gain values separated by space: ").split()))       #-5 1 5 0 -7
sol = Solution()
print("Highest Altitude:", sol.largestAltitude(gain))   #1
