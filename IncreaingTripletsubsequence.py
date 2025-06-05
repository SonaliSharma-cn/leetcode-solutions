class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')  
        second = float('inf') 

        for num in nums:
            print(f"Checking: {num}, first: {first}, second: {second}")
            if num <= first:
                first = num
                print(f"Updated first: {first}")
            elif num <= second:
                second = num
                print(f"Updated second: {second}")
            else:
                print("Found triplet!")
                return True  

        return False
input_str = input("Enter the list of numbers separated by space: ")      #2 1 5 0 4 6
nums = list(map(int, input_str.strip().split()))
solution = Solution()
result = solution.increasingTriplet(nums)

print("Result:", result)                                          

#output
'''Checking: 2, first: inf, second: inf
Updated first: 2
Checking: 1, first: 2, second: inf
Updated first: 1
Checking: 5, first: 1, second: inf
Updated second: 5
Checking: 0, first: 1, second: 5
Updated first: 0
Checking: 4, first: 0, second: 5
Updated second: 4
Checking: 6, first: 0, second: 4
Found triplet!
Result: True'''