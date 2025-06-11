from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        if set(count1.keys()) != set(count2.keys()):
            return False

        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True


if __name__ == "__main__":
    word1 = input("Enter first word: ")      #abc
    word2 = input("Enter second word: ")      #bca

    sol = Solution()
    result = sol.closeStrings(word1, word2)
    print("Are the two strings close?:", result)       #True
