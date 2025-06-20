class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
solution = Solution()
result = solution.gcdOfStrings(str1, str2)
print("Largest string that divides both:", result)