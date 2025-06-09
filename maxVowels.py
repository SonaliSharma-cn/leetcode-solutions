class Solution:

    # 1. Maximum Number of Vowels in a Substring of Given Length
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_vowels = 0
        current_count = 0

        for i in range(k):
            if s[i] in vowels:
                current_count += 1
        max_vowels = current_count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1
            max_vowels = max(max_vowels, current_count)

        return max_vowels

# ✅ Create object of the class
sol = Solution()

print("\n--- Question 1: Max Vowels in Substring ---")
s = input("Enter the string: ")
k1 = int(input("Enter k (length of substring): "))
print("Maximum vowels in a substring:", sol.maxVowels(s, k1))
