class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

input_string = input("Enter a sentence: ")    #me like cake
solution = Solution()
result = solution.reverseWords(input_string)
print("Reversed words:", result)                #cake like me
