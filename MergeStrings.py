class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        result=""
        while i <len(word1) or j<len(word2):
           if i<len(word1):
            result+=word1[i]
            i+=1

           if j<len(word2):
            result+=word2[j]
            j+=1

        return result
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

sol = Solution()
result = sol.mergeAlternately(word1, word2)

print("Merged string:", result)
